import ollama
import requests

modelName = "mistral:instruct"

def comment_code(prompt: str) -> str:
    #prompt += "\n "
    
    print("Sending prompt to Ollama...")
    response = ollama.chat(model=modelName, messages=[{ "role": "user", "content": prompt }])
    print(response)
    result = response['message']['content'].strip()
    
    print("Response received.")
    
    return result

def generate(prompt) -> str:
    output = ""
    if not is_ollama_running():
        output = comment_code(prompt)
    return output

def is_ollama_running():
    try:
        return True
    except:
        return False