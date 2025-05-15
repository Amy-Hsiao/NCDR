# modules/shared_model.py
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_id = r"C:\\Users\\user\\Desktop\\ncdr_integration\\LLM\\Llama3-TAIDE-LX-8B-Chat-Alpha1"

def get_llm_pipeline():
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id, torch_dtype="auto", device_map="auto"
    )
    return pipeline("text-generation", model=model, tokenizer=tokenizer)


