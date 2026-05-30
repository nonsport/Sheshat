import aiohttp
from core.config import S_K, A_K
from core.network import fetch_json

NAME = "IP & Infrastructure Search"
PROMPT = "Введите IP: "

async def execute(ip: str):
    async with aiohttp.ClientSession() as session:
        shodan = await fetch_json(session, f"https://api.shodan.io/shodan/host/{ip}", params={"key": S_K})
        abuse = await fetch_json(session, "https://api.abuseipdb.com/api/v2/check", headers={"Key": A_K}, params={"ipAddress": ip})
        return {"Shodan": shodan, "AbuseIPDB": abuse}
