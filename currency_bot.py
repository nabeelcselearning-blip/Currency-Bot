import requests


def get_exchange_rate():
    # Our new backup API URL. This gets all rates for USD.
    url = "https://open.er-api.com/v6/latest/USD"

    # 1. Send a 'GET' request to the server
    response = requests.get(url)

    # 2. Print the raw text the server sends back
    # print(response.text)

    # Lets do parsing
    # 1. Convert the raw JSON text into a Python dictionary
    data = response.json()
    # 2. Extract our specific currency.
    # Look closely at the data, the currencies are stored inside a 'rates' container.
    inr_rate = data["rates"]["INR"]

    print(f"Success! 1 USD is currently: {inr_rate} INR")

    # We return the value so we can use it in the next step
    return inr_rate


get_exchange_rate()
