import aiohttp
from core.config import N_K
from core.network import fetch_json

# Настройки модуля для автозагрузчика Seshat
NAME = "Phone & Identity Search"
PROMPT = "Введите Номер телефона: "

async def execute(phone: str):
    """
    Выполняет асинхронный запрос к API Numverify для проверки 
    информации о мобильном номере телефона.
    """
    async with aiohttp.ClientSession() as session:
        # Используем общую функцию fetch_json из ядра и ключ N_K из конфигурации
        num = await fetch_json(
            session, 
            "http://apilayer.net/api/validate", 
            params={"access_key": N_K, "number": phone}
        )
        
        # Возвращаем результат в едином формате для построения красивого дерева Rich
        return {"Numverify": num}

