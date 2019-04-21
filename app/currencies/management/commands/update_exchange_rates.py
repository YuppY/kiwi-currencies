from django.core.management.base import BaseCommand

from currencies.download_exchange_rates import download_exchange_rates
from currencies.models import ExchangeRate


class Command(BaseCommand):
    help = "Updates the cache of exchange rates"

    def handle(self, *_args, **_kwargs):
        rates = download_exchange_rates()
        ExchangeRate.objects.update(rates)
