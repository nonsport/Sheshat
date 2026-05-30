import aiohttp

NAME = "Subdomain Scanner (Free)"
PROMPT = "Введите Домен: "

async def execute(domain: str):
    async with aiohttp.ClientSession() as session:
        url = f"https://crt.sh/?q={domain}&output=json"
        try:
            async with session.get(url, timeout=15) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    subdomains = set()
                    for item in data:
                        name = item.get("name_value", "")
                        for sub in name.split("\n"):
                            sub = sub.replace("*.", "").strip()
                            if sub and sub.endswith(domain):
                                subdomains.add(sub)
                    return {"Subdomains_Found": sorted(list(subdomains))}
                return {"Subdomains_Found": {"error": f"HTTP {resp.status}"}}
        except Exception as e:
            return {"Subdomains_Found": {"error": str(e)}}