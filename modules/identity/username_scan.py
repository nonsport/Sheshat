import aiohttp
import re
from core.config import get_headers

NAME = "Username Global Scan"
PROMPT = "Введите Username: "

async def execute(username: str):
    sites = {
        "GitHub": {"url": f"https://github.com/{username}"},
        "Telegram": {"url": f"https://t.me/{username}", "must_contain": 'tgme_page_extra'}, 
        "VKontakte": {"url": f"https://vk.com/{username}"},
        "Steam": {"url": f"https://steamcommunity.com/id/{username}", "not_found": "The specified profile could not be found"},
        "Chess.com": {"url": f"https://www.chess.com/member/{username}"},
        "Reddit": {"url": f"https://www.reddit.com/user/{username}"},
        "Habr": {"url": f"https://habr.com/ru/users/{username}/", "not_found": "Страница не найдена"},
        "Pikabu": {"url": f"https://pikabu.ru/@{username}", "not_found": "Ошибка 404"},
        "Linktree": {"url": f"https://linktr.ee/{username}"},
        "TryHackMe": {"url": f"https://tryhackme.com/p/{username}", "not_found": "User not found"},
        "Pastebin": {"url": f"https://pastebin.com/u/{username}", "not_found": "Not Found"}
    }
    results = {}
    
    async with aiohttp.ClientSession(headers=get_headers()) as session:
        for name, config in sites.items():
            url = config["url"]
            try:
                async with session.get(url, timeout=7) as resp:
                    if resp.status == 200:
                        html = await resp.text()
                        
                        if "not_found" in config and config["not_found"] in html:
                            results[name] = {"Status": "Не найден (Ложный 200 OK)"}
                            continue
                        if "must_contain" in config and config["must_contain"] not in html:
                            results[name] = {"Status": "Не найден (Ложный 200 OK)"}
                            continue
                        
                        title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
                        title = title_match.group(1).strip() if title_match else "Нет заголовка"
                        
                        desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
                        bio = desc_match.group(1).strip() if desc_match else "Описание скрыто"
                        
                        results[name] = {
                            "Status": "Найден",
                            "URL": url,
                            "Title": title,
                            "Bio": bio[:100] + "..." if len(bio) > 100 else bio
                        }
                    elif resp.status == 404:
                        results[name] = {"Status": "Не найден (HTTP 404)"}
                    else:
                        results[name] = {"Status": f"Не найден (HTTP {resp.status})"}
            except Exception:
                results[name] = {"Status": "Ошибка соединения"}
                
    return {"Deep_OSINT_Scan": results}