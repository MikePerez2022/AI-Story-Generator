import ollama
import requests

modelName = "codellama:7b"

def comment_code(code: str) -> str:
    prompt = f"""Insert descriptive comments into this code so an amature can understand the code.
    Original code:
    {code}
    Please output the commented version of the code:
    """
    
    print("Sending prompt to Ollama...")
    response = ollama.chat(model=modelName, messages=[{ "role": "user", "content": prompt }])
    result = response['message']['content'].strip()
    
    # try:
    #     if result.startswith("'''") and result.endswith("'''"):
    #         result = result[3:-3].strip()
    #     elif result.startswith("```python") and result.endswith("```"):
    #         result = result[9:-3].strip()
    #     elif result.startswith("```") and result.endswith("```"):
    #         result = result[3:-3].strip()
    # except Exception as e:
    #     return f"Error: {e}"
    
    print("Response received.")
    
    return result

def AIComment(code) -> str:
    output = ""
    if not is_ollama_running():
        output = comment_code(code)
    return output

def is_ollama_running():
    try:
        #requests.get("http://localhost:11434")
        return True
    except:
        return False