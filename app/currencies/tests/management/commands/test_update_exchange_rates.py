import pytest
from django.core import management

from currencies.models import ExchangeRate
from currencies.test_utils import mock_exchange_rates_source


@pytest.mark.django_db
def test_update_exchange_rates():
    ExchangeRate.objects.create(symbol="FOO", value=1.5)

    with mock_exchange_rates_source(rates={"FOO": 1, "BAR": 10}):
        management.call_command("update_exchange_rates")

    assert tuple(ExchangeRate.objects.order_by("symbol").values_list("symbol", "value")) == (("BAR", 10), ("FOO", 1))
