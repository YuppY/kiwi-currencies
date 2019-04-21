from contextlib import contextmanager

import requests_mock

from currencies.download_exchange_rates import EXCHANGE_RATES_URL


@contextmanager
def mock_exchange_rates_source(rates=None, status_code=None):
    """
    Mocks exchange rates source for tests
    """
    with requests_mock.mock() as m_requests:
        kwargs = {}
        if rates is not None:
            kwargs["json"] = {"rates": rates}
        if status_code is not None:
            kwargs["status_code"] = status_code
        m_requests.get(EXCHANGE_RATES_URL, **kwargs)
        yield m_requests
