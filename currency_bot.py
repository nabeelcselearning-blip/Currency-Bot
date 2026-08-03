import requests


def get_exchange_rate():
    # Our new backup API URL. This gets all rates for USD.
    url = "https://open.er-api.com/v6/latest/USD"

    response = requests.get(url)

    print(response.text)


get_exchange_rate()
