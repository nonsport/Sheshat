from prompt_toolkit import PromptSession

NAME = "Base64 Encoder / Decoder"
PROMPT = None  # Отключаем дефолтный промпт ядра, так как у нас своя логика внутри

async def execute():
    # Создаем асинOverlay-сессию для ввода внутри модуля
    session = PromptSession()
    
    # Используем prompt_async вместо обычного prompt
    action = await session.prompt_async("❖ [1] Encode | [2] Decode : ")
    text = await session.prompt_async("❖ Введите текст: ")
    
    import base64
    if action.strip() == '1':
        result = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        return {"Base64_Encode": {"Result": result}}
    elif action.strip() == '2':
        try:
            result = base64.b64decode(text.encode('utf-8')).decode('utf-8')
            return {"Base64_Decode": {"Result": result}}
        except Exception:
            return {"Base64_Decode": {"Error": "Невалидный Base64 код"}}
            
    return {"Base64": {"Error": "Неверный выбор операции"}}
