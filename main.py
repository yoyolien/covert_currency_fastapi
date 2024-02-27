from fastapi import FastAPI

app = FastAPI()

exchange_rate = {
    "TWD": {
        "TWD": 1,
        "JPY": 3.669,
        "USD": 0.03281
    },
    "JPY": {
        "TWD": 0.26956,
        "JPY": 1,
        "USD": 0.00885
    },
    "USD": {
        "TWD": 30.444,
        "JPY": 111.801,
        "USD": 1
    },
}


@app.get("/")
async def convert(source: str, target: str, amount: str):
    try:
        rate = exchange_rate[source][target]
        amount = float(amount[1:].replace(",", ""))
        amount = amount * rate
        amount = round(amount, 2)
        amount = "{:,}".format(amount)
        return {"message": "success",
                "amount": f"${amount}"
                }
    except Exception as e:
        return {"message": str(e)}
