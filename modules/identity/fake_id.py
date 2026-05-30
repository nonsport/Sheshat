from faker import Faker

NAME = "Generate Fake Identity"
PROMPT = "Введите локаль [Enter=ru_RU]: "

async def execute(target: str):
    locale = target.strip() if target.strip() else 'ru_RU'
    fake = Faker(locale)
    return {
        "Fake_Profile": {
            "Name": fake.name(),
            "Address": fake.address().replace('\n', ', '),
            "Phone": fake.phone_number(),
            "Email": fake.email(),
            "Company": fake.company(),
            "IP": fake.ipv4()
        }
    }
