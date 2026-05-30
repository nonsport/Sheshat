NAME = "Google Dorks Generator"
PROMPT = "Введите Домен для Dorks: "

async def execute(domain: str):
    return {"Google_Dorks": [
        {"Target": "Config", "URL": f"https://www.google.com/search?q=site:{domain}+ext:env+OR+ext:sql"},
        {"Target": "Login", "URL": f"https://www.google.com/search?q=site:{domain}+inurl:login+OR+inurl:admin"}
    ]}
