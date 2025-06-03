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

def stream_comment_code(prompt: str, modelName: str):
    print("Sending prompt to Ollama (streaming)...")
    response_stream = ollama.chat(model=modelName, messages=[{"role": "user", "content": prompt}], stream=True)
    for chunk in response_stream:
        content = chunk["message"]["content"] if "message" in chunk and "content" in chunk["message"] else ""
        if modelName == "deepseek-r1":
            content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
        yield content
    print("Streaming response complete.")


def stream_generate(prompt, model=""):
    if model == "":
        yield "Unsupported Model."
        return
    yield from stream_comment_code(prompt, model)