from core.config import get_headers

async def fetch_json(session, url, headers=None, params=None):
    try:
        async with session.get(url, headers=headers or get_headers(), params=params, timeout=12) as response:
            if response.status == 200:
                return await response.json()
            return {"error": f"HTTP {response.status}"}
    except Exception as e:
        return {"error": str(e)}
