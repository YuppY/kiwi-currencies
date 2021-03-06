import pytest

from currencies.models import ExchangeRate

pytestmark = pytest.mark.django_db


def test_get_rate_404(client):
    assert client.get("/rates/FOO/BAR/").status_code == 404

    ExchangeRate.objects.create(symbol="FOO", value=1)
    assert client.get("/rates/FOO/BAR/").status_code == 404


def test_get_rate_400(client):
    ExchangeRate.objects.create(symbol="FOO", value=1)
    ExchangeRate.objects.create(symbol="BAR", value=10)

    assert client.get("/rates/FOO/BAR/?value=invalid").status_code == 400


def test_get_rate(client):
    ExchangeRate.objects.create(symbol="FOO", value=1)
    ExchangeRate.objects.create(symbol="BAR", value=10)

    response = client.get("/rates/FOO/BAR/")
    assert response.status_code == 200
    assert response.data == {"source": {"value": 1, "symbol": "FOO"}, "result": {"value": 10, "symbol": "BAR"}}

    response = client.get("/rates/FOO/BAR/?value=1.5")
    assert response.status_code == 200
    assert response.data == {"source": {"value": 1.5, "symbol": "FOO"}, "result": {"value": 15, "symbol": "BAR"}}
