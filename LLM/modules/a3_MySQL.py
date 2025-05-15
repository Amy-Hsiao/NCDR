from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
from .a1_model import get_llm_pipeline
# model_id = r"C:\\Users\\user\\Desktop\\ncdr_integration\\LLM\\Llama3-TAIDE-LX-8B-Chat-Alpha1"
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForCausalLM.from_pretrained(
#     model_id, torch_dtype="auto", device_map="auto"
# )

# 資料庫
earthquake_resources = {
    "台南市": {
        "5.5,發生機率0.2": {
            "medical_resources": {
                "衛生福利部台南醫院": 50,
                "永川醫院": 30
            },
            "gathering_point_trucks": {
                "南台科技大學": 5,
                "崑山科技大學": 3
            }
        },
        "5.7,發生機率0.5": {
            "medical_resources": {
                "衛生福利部台南醫院": 60,
                "永川醫院": 40
            },
            "gathering_point_trucks": {
                "南台科技大學": 6,
                "崑山科技大學": 4
            }
        },
        "6.0,發生機率0.1": {
            "medical_resources": {
                "衛生福利部台南醫院": 80,
                "永川醫院": 50
            },
            "gathering_point_trucks": {
                "南台科技大學": 8,
                "崑山科技大學": 5
            }
        },
        "7.3,發生機率0.2": {
            "medical_resources": {
                "衛生福利部台南醫院": 500,
                "永川醫院": 300
            },
            "gathering_point_trucks": {
                "南台科技大學": 50,
                "崑山科技大學": 30
            }
        }
    },
}

def get_resources_for_city(city, earthquake_resources):
    city_data = earthquake_resources.get(city)
    if not city_data:
        return f"無法找到城市 {city} 的資源資料。", ""

    medical_summary = {}
    truck_summary = {}
    output_text = f"查詢城市：{city} 的資源需求如下：\n"
    for magnitude, resources in city_data.items():
        output_text += f"\n地震級數 {magnitude}:\n"

        med_data = resources.get("medical_resources", {})
        truck_data = resources.get("gathering_point_trucks", {})

        output_text += "  醫療資源：\n"
        for loc, num in med_data.items():
            output_text += f"    {loc} 需 {num} 包\n"
            medical_summary.setdefault(loc, []).append(num)

        output_text += "  卡車數量：\n"
        for loc, num in truck_data.items():
            output_text += f"    {loc} 需 {num} 輛\n"
            truck_summary.setdefault(loc, []).append(num)

    return output_text, (medical_summary, truck_summary)

def find_worst_case(data_dict):
    return {loc: max(values) for loc, values in data_dict.items()}

def make_prompt(city, output_text, med_max, truck_max):
    med_str = "\n".join([f"{k}：{v} 包" for k, v in med_max.items()])
    truck_str = "\n".join([f"{k}：{v} 輛" for k, v in truck_max.items()])

    prompt = f"""
你是一位防災指揮官，根據下列地震等級與發生機率對資源需求資料進行分析。
請完成以下任務：

1. 對每個醫院和集結點，列出最壞情況（最大需求）。
2. 依據最壞情況，使用「Min-Max 決策原則」選擇風險最小的醫院與集結點。
3. 請簡要說明你的選擇理由，並提出具體的資源配置建議。

=== 台南市防災資源需求資料 ===
{output_text}

=== 醫院最壞情況（最大需求） ===
{med_str}

=== 集結點最壞情況（最大需求） ===
{truck_str}
"""
    return prompt

# pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
llm_pipeline = get_llm_pipeline()
def smart_summarize(prompt):
    response = llm_pipeline(prompt, max_length=1500, truncation=True, num_return_sequences=1)
    return response[0]['generated_text'].replace(prompt.strip(), "").strip()


def clean_response(response, prompt):
        """
        清理語言模型生成的回應，刪除與輸入 prompt 重複的部分。
        """
        cleaned = response.replace(prompt.strip(), "").strip()
        return cleaned

def main():
    city = "台南市"
    output_text, (med_data, truck_data) = get_resources_for_city(city, earthquake_resources)
    # print("數學模型運算各集結點資源需求如下： ")
    # print(output_text)

    med_max = find_worst_case(med_data)
    truck_max = find_worst_case(truck_data)

    final_prompt = make_prompt(city, output_text, med_max, truck_max)
    # print("根據Min-Max 決策原則總結建議如下： ")
    results=smart_summarize(final_prompt)
    # print(clean_response(results,final_prompt))

    cleaned = clean_response(results,final_prompt)
    final_output = f"""
    數學模型運算各集結點資源需求如下：\n
    {output_text}\n
    根據Min-Max 決策原則總結建議如下：\n
    {cleaned}\n
    """
    print(final_output)
    return final_output


if __name__ == "__main__":
    main()
    torch.cuda.empty_cache()
