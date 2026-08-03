import requests


def get_exchange_rate():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url)

    # 1. Convert the raw JSON text into a Python dictionary
    data = response.json()

    # 2. Extract our specific currency.
    # If you look closely at the data, the currencies are stored inside a 'rates' container.
    inr_rate = data["rates"]["INR"]

    print(f"Success! 1 USD is currently: {inr_rate} INR")

    # We return the value so we can use it in the next step
    return inr_rate


# Run it to test
get_exchange_rate()
