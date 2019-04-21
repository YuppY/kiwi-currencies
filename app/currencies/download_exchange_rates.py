import requests
from django.conf import settings

EXCHANGE_RATES_URL = "https://openexchangerates.org/api/latest.json"


def download_exchange_rates():
    response = requests.get(
        EXCHANGE_RATES_URL,
        params=(
            ("app_id", settings.CURRENCIES_OPENEXCHANGERATES_APP_ID),
            ("symbols", ",".join(settings.CURRENCIES_SYMBOLS)),
        ),
    )
    response.raise_for_status()
    return response.json()["rates"]
