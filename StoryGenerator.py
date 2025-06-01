import ollama
import re

# modelName = "mistral:instruct"

def comment_code(prompt: str, modelName:str) -> str:
    print("Sending prompt to Ollama...")
    response = ollama.chat(model=modelName, messages=[{ "role": "user", "content": prompt }])
    print(response)
    result = response['message']['content'].strip()
    
    if(modelName == "deepseek-r1"):
        result = re.sub(r"<think>.*?</think>", "", result, flags=re.DOTALL).strip()
    
    print("Response received.")
    
    return result

def generate(prompt, model = "") -> str:
    if(model == ""): return "Unsupported Model."
    output = comment_code(prompt, model)
    return output