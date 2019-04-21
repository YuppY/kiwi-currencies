from django.urls import path

from currencies import views


urlpatterns = [path("rates/<source_currency_symbol>/<target_currency_symbol>/", views.rate, name="rate")]
