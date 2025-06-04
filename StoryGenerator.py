import ollama
import re

# modelName = "mistral:instruct"

def _clean_deepseek_think(content: str, modelName: str) -> str:
    if modelName == "deepseek-r1":
        return re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
    return content

def comment_code(prompt: str, modelName:str) -> str:
    print("Sending prompt to Ollama...")
    response = ollama.chat(model=modelName, messages=[{ "role": "user", "content": prompt }])
    print(response)
    result = response['message']['content'].strip()
    result = _clean_deepseek_think(result, modelName)
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
        content = _clean_deepseek_think(content, modelName)
        yield content
    print("Streaming response complete.")

def stream_generate(prompt, model=""):
    if model == "":
        yield "Unsupported Model."
        return
    yield from stream_comment_code(prompt, model)

def nonstream_generate(prompt, model=""):
    if model == "":
        return "Unsupported Model."
    return comment_code(prompt, model)