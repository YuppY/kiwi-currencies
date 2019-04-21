import pytest
import requests
from django.test import override_settings

from currencies.download_exchange_rates import EXCHANGE_RATES_URL, download_exchange_rates
from currencies.test_utils import mock_exchange_rates_source


@pytest.fixture(autouse=True)
def currencies_settings():
    with override_settings(
        CURRENCIES_OPENEXCHANGERATES_APP_ID="openexchangerates_app_id", CURRENCIES_SYMBOLS=("FOO", "BAR", "USD")
    ):
        yield


def test_download_exchange_rates():
    with mock_exchange_rates_source(rates={"FOO": 10, "BAR": 1.5, "USD": 1}) as m_requests:
        assert download_exchange_rates() == {"FOO": 10, "BAR": 1.5, "USD": 1}

    assert m_requests.call_count == 1
    assert m_requests.last_request.method == "GET"

    assert m_requests.last_request.url == "{}?app_id=openexchangerates_app_id&symbols=FOO%2CBAR%2CUSD".format(
        EXCHANGE_RATES_URL
    )


def test_download_exchange_rates_raising():
    with mock_exchange_rates_source(status_code=500) as m_requests, pytest.raises(requests.HTTPError):
        download_exchange_rates()

    assert m_requests.call_count == 1
