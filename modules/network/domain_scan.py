import aiohttp
from core.config import H_K
from core.network import fetch_json

NAME = "Domain & Email Search"
PROMPT = "Введите Домен: "

async def execute(domain: str):
    async with aiohttp.ClientSession() as session:
        hunter = await fetch_json(session, "https://api.hunter.io/v2/domain-search", params={"domain": domain, "api_key": H_K})
        return {"Hunter_Emails": hunter}