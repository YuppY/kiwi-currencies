from django.db import models


class ExchangeRateManager(models.Manager):
    def update(self, rates):
        for symbol, rate in rates.items():
            self.update_or_create(symbol=symbol, defaults={"value": rate})


class ExchangeRate(models.Model):
    symbol = models.CharField(max_length=128, primary_key=True)
    value = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    objects = ExchangeRateManager()

    def __str__(self):
        return self.symbol

    def convert_to_base(self, source_value):
        return source_value / self.value

    def convert_from_base(self, base_value):
        return base_value * self.value
