# kiwi-currencies
Currency exchange rate converter.

## Running

1. Register at https://openexchangerates.org/ to get App ID
2. Enter your App ID into `app/app/settings.py`:
```python
CURRENCIES_OPENEXCHANGERATES_APP_ID = '<App ID>'
```
3. Install Docker Compose

4. Initialize containers and the database:
```bash
docker-compose run app wait-for-it db:5432 -- ./manage.py migrate
docker-compose run app ./manage.py update_exchange_rates
```
5. Start the application:
```bash
docker-compose up
```

6. API endpoint will be available at http://localhost:8000/rates/USD/EUR/?value=100

## Running tests

```bash
docker-compose run app pytest --cov
```

## Admin interface access

1. Create a superuser:
```bash
docker-compose run app ./manage.py createsuperuser
```

2. Login into the admin interface of the running app via http://localhost:8000/admin/

## Configuration

- `crontab` — cron schedule of exchange rates caching task;
- `app/app/settings.py`:
  - `CURRENCIES_OPENEXCHANGERATES_APP_ID` — App ID of openexchangerates.org;
  - `CURRENCIES_SYMBOLS` — list of supported currency symbols.
