import requests
import json

URL = 'https://api.monobank.ua/bank/currency'


response = requests.get(URL)
data = json.loads(response.text)


USD_sale = float(data[0]['rateSell'])
USD_buy = float(data[0]['rateBuy'])


EUR_sale = float(data[1]['rateSell'])
EUR_buy = float(data[1]['rateBuy'])


RUB_sale = float(data[2]['rateSell'])
RUB_buy = float(data[2]['rateBuy'])