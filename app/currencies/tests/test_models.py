from django.db.utils import IntegrityError
import pytest

from currencies.models import ExchangeRate


class TestExchangeRateManager:
    @pytest.mark.django_db
    def test_update(self):
        ExchangeRate.objects.create(symbol='USD', value=1)
        ExchangeRate.objects.create(symbol='CZK', value=20)

        ExchangeRate.objects.update({'USD': 1.1, 'EUR': 1.3})
        assert tuple(
            ExchangeRate.objects.order_by('symbol').values_list('symbol', 'value')
        ) == (
            ('CZK', 20), ('EUR', 1.3), ('USD', 1.1),
        )


class TestExchangeRate:
    def test_str(self):
        assert str(ExchangeRate(symbol='USD')) == 'USD'

    def test_convert_to_base(self):
        assert ExchangeRate(value=1.5).convert_to_base(15) == 10

    def test_convert_from_base(self):
        assert ExchangeRate(value=1.5).convert_from_base(10) == 15

    @pytest.mark.django_db
    @pytest.mark.parametrize('value', (0, -2))
    def test_constraint(self, value):
        with pytest.raises(IntegrityError):
            ExchangeRate.objects.create(symbol='USD', value=value)
