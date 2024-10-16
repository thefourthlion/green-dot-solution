import requests

def converter(from_currency, to_currency, amount): 
    r = requests.get('https://api.exchangerate-api.com/v4/latest/'+from_currency)
    rates = r.json()
    
    return amount * rates['rates'][to_currency]

print("Supported currencies: USD, EUR, GBP, JPY, etc.")
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
amount = float(input("Amount: "))

result = converter(from_currency, to_currency, amount)

print(f'{amount} {from_currency} is equal to {result} {to_currency}')