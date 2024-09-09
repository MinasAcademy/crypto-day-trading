import ccxt
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")


binance = ccxt.binance({
    'apiKey': api_key,
    'secret': secret_key,
    'enableRateLimit': True, 
})

def calculate_total_balance_in_usd():
    try:
        # Fetch balance
        balance = binance.fetch_balance()
        total_usd_balance = 0.0

        # Iterate over each asset in the balance
        for asset, asset_balance in balance['total'].items():
            if asset == 'USDT':
                total_usd_balance += asset_balance  # USDT is already in USD
            else:
                # Fetch the current price of the asset in USDT
                try:
                    ticker = binance.fetch_ticker(f'{asset}/USDT')
                    last_price = ticker['last']
                    
                    # Check if the price is not None and then calculate the value
                    if last_price is not None:
                        asset_usd_value = asset_balance * last_price
                        total_usd_balance += asset_usd_value
                    else:
                        print(f"Price for {asset}/USDT is not available. Skipping.")

                except ccxt.BaseError as e:
                    print(f"Couldn't fetch the price for {asset}/USDT. Skipping. Error: {e}")

        return total_usd_balance

    except ccxt.BaseError as e:
        print(f"An error occurred: {e}")
        return None


# Get the total balance in USD
total_balance_usd = calculate_total_balance_in_usd()

if total_balance_usd is not None:
    print(f"Total Balance in USD: ${total_balance_usd:.2f}")
