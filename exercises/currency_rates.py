import requests

from config import CURRENCY_API_URL


def get_usd_rate(target):
    response = requests.get(CURRENCY_API_URL)
    data = response.json()
    return data["rates"][target]
