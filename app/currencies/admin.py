from django.contrib import admin

from currencies.models import ExchangeRate


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ("symbol", "value", "updated_at")
    readonly_fields = ("updated_at",)
