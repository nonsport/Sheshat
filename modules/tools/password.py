import random
import string
from prompt_toolkit import prompt

NAME = "Password Generator"
PROMPT = None

async def execute():
    try:
        length_input = prompt("❖ Длина пароля (6-32): ")
        length = int(length_input)
        length = max(6, min(32, length))
        
        all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+="
        password = [random.choice(c) for c in (string.ascii_lowercase, string.ascii_uppercase, string.digits, "!@#$%^&*()-_+=")]
        password += [random.choice(all_chars) for _ in range(length - 4)]
        random.shuffle(password)
        
        pwd = ''.join(password)
        return {"Password_Generator": {"Generated": pwd}}
    except ValueError:
        return {"Password_Generator": {"Error": "Введите число!"}}
