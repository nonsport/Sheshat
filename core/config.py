import base64
import random

def d(b): return base64.b64decode(b).decode("utf-8")

# Зашифрованные ключи
S_K = d("VUZ1RWE1V3VQN3lqbEl0UFZucTh6NGRudTRGcGdXV2U=")
C_K = d("Y2Vuc3lzX0VBNGtNVHBhX0JWbVp4ODVvVmZ4SGoyaTF6TFliZm5RZw==")
H_K = d("Yzg0NDBlZjliNzIyZmNhNjg2M2UzNzc3M2YzODE4NTY2ZTk3MjUyNg==")
A_K = d("MGUxMWQ5MjVhY2RmNjcxMmM3MGZlMmVkN2Q3MDkzODQzMTRlNzU2ODhjMmU=")
N_K = d("NDkwYTE5NzliNGE4Y2JiNmJjNDc0YTlmMjU2OTcwYjY=")

UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
]

def get_headers():
    return {
        "User-Agent": random.choice(UAS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5"
    }
