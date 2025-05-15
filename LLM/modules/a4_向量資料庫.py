from . import a2_earthquake_info
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import json
import torch
from .a1_model import get_llm_pipeline

# 初始化 Pinecone
PINECONE_API_KEY = "pcsk_3gAa4p_TuAWZksvawiobafLsJuvNzXbwCZ3p6ihuwcm2goRNBxjVx5n3VRBJkHZk1vnfYn"
pinecone_client = Pinecone(api_key=PINECONE_API_KEY)

# 索引與命名空間
index_name = "ncdr-data"
namespace = "history-disaster-info"
index = pinecone_client.Index(index_name)

# 嵌入模型與 LLM 初始化
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
model_id = r"C:\\Users\\user\\Desktop\\ncdr_integration\\LLM\\Llama3-TAIDE-LX-8B-Chat-Alpha1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto", device_map="auto")
# llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
llm_pipeline = get_llm_pipeline()

def retrieve_similar_disasters(user_query):
    query_vector = embedding_model.encode(user_query).tolist()
    results = index.query(
        vector=query_vector,
        top_k=1,
        include_metadata=True,
        namespace=namespace
    )
    return results["matches"] if results["matches"] else None

def generate_rag_response(user_query, matches):
    if not matches:
        return "未找到相似的歷史災害資料，請提供更多詳細資訊。"

    context = "\n".join([
        f"災害名稱：{match.metadata.get('災害名稱', '未知')}\n"
        f"震央：{match.metadata.get('震央', '未知')}\n"
        f"震度：{match.metadata.get('震度', '未知')}\n"
        f"地震規模：{match.metadata.get('地震規模', '未知')}\n"
        f"震源深度：{match.metadata.get('震源深度', '未知')} 公里\n"
        f"PGA：{match.metadata.get('PGA', '未知')} gal\n"
        f"PGV：{match.metadata.get('PGV', '未知')} cm/s\n"
        f"影響範圍：{match.metadata.get('影響範圍', '未知')}\n"
        f"應變策略：{json.loads(match.metadata.get('應變策略', '{}'))}\n"
        for match in matches
    ])

    prompt = (
    f"""目前的地震情況如下：{user_query}
    請根據以下歷史災害資料提供一段完整的決策建議報告。
    請從『此次地震情況概述』開始，接著『比對過往的災害資料』，最後『根據經驗提供行動建議』。
    以下是可供參考的歷史資料：{context}
    "請以完整段落形式回應，例如：
    "「目前地震發生於⋯⋯，震央位於⋯⋯，根據過往的⋯⋯地震經驗，建議採取以下措施⋯⋯」""")
    response = llm_pipeline(prompt, max_new_tokens=4096, num_return_sequences=1)
    generated = response[0]['generated_text']
    cleaned = clean_response(generated, prompt)   
    return cleaned

def clean_response(response, prompt):
        """
        清理語言模型生成的回應，刪除與輸入 prompt 重複的部分。
        """
        cleaned = response.replace(prompt.strip(), "").strip()
        return cleaned

def vectorize_and_decide():
    
    
    summary = a2_earthquake_info.main()

    # print("=== 地震資訊摘要如下 ===")
    # print(summary)

    # 進行相似地震資料檢索與生成應變建議
    matches = retrieve_similar_disasters(summary)
    decision = generate_rag_response(summary, matches)

    final_output = f"""
    應變建議如下：\n
    {decision}\n
    """
    print(final_output)
    return final_output

if __name__ == "__main__":
    vectorize_and_decide()
    del model
    torch.cuda.empty_cache()
