from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("API_KEY")

def exchange_currency(amount, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}/{amount}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['result'] == 'success':
            converted_amount = data['conversion_result']
            print(f"\n💱 {amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            print("❌ Error in conversion:", data['error-type'])
    else:
        print("❌ Network error or invalid request.")

#== MAIN ==

print("💵Currency Exchange💱\n")

currency_codes = {
    "USD": "United States",
    "NGN": "Nigeria",
    "GBP": "United Kingdom",
    "EUR": "European Union",
    "CAD": "Canada",
    "AUD": "Australia",
    "JPY": "Japan",
    "CNY": "China",
    "INR": "India",
    "ZAR": "South Africa",
    "KES": "Kenya",
    "GHS": "Ghana",
    "EGP": "Egypt",
    "CHF": "Switzerland",
    "RUB": "Russia",
    "BRL": "Brazil",
    "MXN": "Mexico",
    "KRW": "South Korea",
    "TRY": "Turkey",
    "SAR": "Saudi Arabia",
    "AED": "United Arab Emirates",
    "SGD": "Singapore",
    "MYR": "Malaysia",
    "PHP": "Philippines",
    "THB": "Thailand",
    "IDR": "Indonesia",
    "PKR": "Pakistan",
    "BDT": "Bangladesh",
    "QAR": "Qatar\n"
}

print("Supported currencies:")
for code, country in currency_codes.items():
    print(f"{code} - {country}")

from_currency = input("From currency (e.g. NGN): ").upper()
to_currency = input("To currency (e.g. USD): ").upper()

try:
    amount = float(input("Amount: "))
    exchange_currency(amount, from_currency, to_currency)
except ValueError:
    print("❌ Invalid amount. Please enter a number.")
