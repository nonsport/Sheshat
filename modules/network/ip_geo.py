import aiohttp
from core.network import fetch_json

NAME = "IP Geolocation (Free)"
PROMPT = "Введите IP: "

async def execute(ip: str):
    async with aiohttp.ClientSession() as session:
        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,mobile,proxy,hosting"
        data = await fetch_json(session, url)
        return {"IP_Geo_Free": data}
