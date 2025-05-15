
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
import torch
from .a1_model import get_llm_pipeline
# model_id = r"C:\Users\user\Desktop\ncdr_integration\LLM\Llama3-TAIDE-LX-8B-Chat-Alpha1"
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForCausalLM.from_pretrained(
#     model_id, torch_dtype="auto", device_map="auto"
# )#.to(device="cuda" if torch.cuda.is_available else "cpu")

# pipe = pipeline("text-generation", model, tokenizer=tokenizer)
llm_pipeline = get_llm_pipeline()
def typesetting(disaster_report):
    #排版
    typesetting_prompt=f"""
    你是一個專門負責將文件變成 Markdown 格式的程式，請依據以下報告書內容進行整理，並生成清晰且結構合理的 Markdown 格式文件。

    要求：
    1. 根據內容邏輯，將標題、段落、列表等適當分類與結構化。
    2. 為標題添加適當層級，例如 #、##、### 等。
    3. 使用有序或無序列表清晰呈現項目內容。
    4. 如果有表格數據，請轉換為 Markdown 表格格式。
    5. 確保生成的 Markdown 文件易於閱讀且具有結構性。

    原始內容：
    ---
    {disaster_report}
    ---

    請生成符合以上要求的 Markdown 文件，確保格式正確並完整反映原始內容。
    """
    
    response = llm_pipeline(typesetting_prompt, max_length=4096, num_return_sequences=1)
    return response[0]['generated_text']

def clean_response(response, prompt):
        """
        清理語言模型生成的回應，刪除與輸入 prompt 重複的部分。
        """
        cleaned = response.replace(prompt.strip(), "").strip()
        return cleaned



def generate_typesetting(disaster_report):
    response = typesetting(disaster_report)
    prompt=f"""
    你是一個專門負責將文件變成 Markdown 格式的程式，請依據以下報告書內容進行整理，並生成清晰且結構合理的 Markdown 格式文件。

    要求：
    1. 根據內容邏輯，將標題、段落、列表等適當分類與結構化。
    2. 為標題添加適當層級，例如 #、##、### 等。
    3. 使用有序或無序列表清晰呈現項目內容。
    4. 如果有表格數據，請轉換為 Markdown 表格格式。
    5. 確保生成的 Markdown 文件易於閱讀且具有結構性。

    原始內容：
    ---
    {disaster_report}
    ---

    請生成符合以上要求的 Markdown 文件，確保格式正確並完整反映原始內容。

    """
    cleaned_response = clean_response(response,prompt)
    return cleaned_response
      

if __name__ == "__main__":
    disaster_report="""
    一、最近地震資訊
    1. 報告內容: 11/20-12:23嘉義縣義竹鄉發生規模4.6有感地震，最大震度嘉義縣義竹、嘉義縣太保市4級。
    2. 報告圖片: https://scweb.cwa.gov.tw/webdata/OLDEQ/202411/2024112012232246496_H.png
    3. 報告備註: 本報告係中央氣象署地震觀測網即時地震資料地震速報之結果。
    4. 報告連結: https://scweb.cwa.gov.tw/zh-tw/earthquake/details/2024112012232246496

    - 臺南市 (臺南市地區): 震度 3級
    - 測站: 白河, 震度: 3級, 距離震央: 18.76 公里
    - 測站: 佳里, 震度: 3級, 距離震央: 19.43 公里
    - 測站: 善化, 震度: 2級, 距離震央: 24.15 公里
    - 測站: 永康, 震度: 2級, 距離震央: 34.27 公里
    - 測站: 新化, 震度: 2級, 距離震央: 38.1 公里
    - 測站: 臺南市, 震度: 2級, 距離震央: 39.38 公里
    - 測站: 東山, 震度: 2級, 距離震央: 28.98 公里
    - 測站: 楠西, 震度: 1級, 距離震央: 35.38 公里

    二、資源分配
    輕度應對（地震5.5~5.9級）
    南台科技大學：(5×0.2+3×0.2)/(0.2+0.5)=4.5個卡車
    崑山科技大學：(3×0.2+4×0.2)/(0.2+0.5)=3.6個卡車
    輕度應對（地震5.10~5.9級）
    南台科技大學：(8×0.1+5×0.1)/(0.1+0.1)=6.5個卡車
    崑山科技大學：(5×0.1+3×0.1)/(0.1+0.1)=4.5個卡車
    重度應對（地震7.0~7.9級）
    南台科技大學：(50×0.2+8×0.1)/(0.2+0.1)=54個卡車
    崑山科技大學：(30×0.2+5×0.1)/(0.2+0.1)=32.5個卡車
    根據計算結果，輕度應對所需卡車數量為南台科技大學4.5個、崑山科技大學3.6個；輕度應對所需卡車數量為南台科技大學6.5個、崑山科技大學4.5個；重度應對所需卡車數量為南台科技大學54個 、崑山科技大學32.5個。請注意，崑山科技大學的重度應對卡車數量為32.5個，由於無法提供半個卡車，因此應取整為33個卡車。故最終結果為：輕度應對（地震5.5~5.9級）南台科技大學4.5個、 崑山科技大學3.6個；輕度應對（地震5.10~5.9級）南台科技大學6.5個、崑山科技大學4.5個；重度應對（地震7.0~7.9級）南台科技大學54個、崑山科技大學33個卡車。

    三、配送路徑規劃
    說明：
    根據所提供的資訊，以下是醫療資源運輸路線的規劃：
    運輸路線：
    起點：崑山科技大學（卡車集結點）
    經過道路：中正北路 → 中山南路 → 永大路 → 復國一路 → 復國二路 → 中華路 → 大灣路 → 鹽行路 → 勝利路 → 文化路
    中繼點：台南市志誠醫院（載取醫療包）
    經過道路：文化路 → 中山南路 → 中正北路
    此路線先從崑山科技大學出發，經由永康區主要道路系統，前往台南市志誠醫院載取醫療包。之後，沿著相反的路線返回崑山科技大學，將醫療包運送至災區 A。請注意，災區名稱尚未確認，請於實際執行前更新為正確的災區名稱此路線先從崑山科技大學出發，經由永康區主要道路系統，前往台南市志誠醫院載取醫療包。之後，沿著相反的路線返回崑山科技大學，將醫療包運送至災區 A。請注意，災區名稱尚未確認，請於實際執行前更新為正確的災區名稱
    """
    response = generate_typesetting(disaster_report)
    print(response)
    torch.cuda.empty_cache()