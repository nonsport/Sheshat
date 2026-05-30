import base64
from prompt_toolkit import prompt

NAME = "Base64 Encoder / Decoder"
PROMPT = None

async def execute():
    action = prompt("❖ [1] Encode | [2] Decode : ")
    text = prompt("❖ Введите текст: ")
    
    if action == '1':
        return {"Base64_Encode": {"Result": base64.b64encode(text.encode('utf-8')).decode('utf-8')}}
    elif action == '2':
        try:
            return {"Base64_Decode": {"Result": base64.b64decode(text.encode('utf-8')).decode('utf-8')}}
        except Exception:
            return {"Base64_Decode": {"Error": "Invalid Base64"}}
            
    return {"Base64": {"Error": "Неверный выбор"}}
