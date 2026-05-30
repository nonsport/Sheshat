import aiohttp

NAME = "Crypto Wallet Check (BTC/ETH)"
PROMPT = "Введите адрес кошелька: "

async def execute(wallet_address: str):
    url = f"https://blockchain.info/rawaddr/{wallet_address}"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    balance_btc = data.get("final_balance", 0) / 100000000
                    tx_count = data.get("n_tx", 0)
                    return {
                        "Crypto_OSINT": {
                            "Address": wallet_address,
                            "Balance (BTC)": f"{balance_btc} BTC",
                            "Total Transactions": tx_count
                        }
                    }
                else:
                    return {"Crypto_OSINT": {"error": "Неверный адрес или лимит запросов"}}
        except Exception as e:
            return {"Crypto_OSINT": {"error": str(e)}}

