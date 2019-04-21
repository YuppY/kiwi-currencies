from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from currencies.models import ExchangeRate


def _parse_float(raw_value, default):
    return float(raw_value) if raw_value else default


@api_view()
def rate(request, source_currency_symbol, target_currency_symbol):
    source_rate = get_object_or_404(ExchangeRate, symbol=source_currency_symbol)
    target_rate = get_object_or_404(ExchangeRate, symbol=target_currency_symbol)

    try:
        value = _parse_float(request.query_params.get("value"), default=1)
    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    result = target_rate.convert_from_base(source_rate.convert_to_base(value))

    return Response(
        {
            "source": {"value": value, "symbol": source_currency_symbol},
            "result": {"value": result, "symbol": target_currency_symbol},
        }
    )
