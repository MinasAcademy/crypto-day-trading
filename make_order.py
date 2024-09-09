import ccxt
from dotenv import load_dotenv
import os
import time

load_dotenv()
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")


exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': secret_key,
    'enableRateLimit': True, 
})

symbol = 'BTC/USDT'
order_amount = 8  # Amount in USDT to spend on each trade

def get_current_price(symbol):
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

def place_market_buy_order(symbol, amount_in_usdt):
    # Fetch the current BTC/USDT price
    price = get_current_price(symbol)
    # Calculate the amount of BTC to buy
    amount = amount_in_usdt / price
    # Place a market buy order
    order = exchange.create_market_buy_order(symbol, amount)
    return order, amount

def place_limit_sell_order(symbol, amount, target_price):
    # Place a limit sell order at the target price
    order = exchange.create_limit_sell_order(symbol, amount, target_price)
    return order

# Main trading loop
while True:
    try:
        current_price = get_current_price(symbol)
        last_trade_price = exchange.fetch_my_trades(symbol)[-1]['price']

        if current_price <= last_trade_price * 0.99:
            # Place a market buy order when price dips by 1%
            print(f"Price dip detected! Current price: {current_price}. Last trade price: {last_trade_price}.")
            buy_order, btc_amount = place_market_buy_order(symbol, order_amount)
            print(f"Market buy order placed: {buy_order}")

            # Calculate the target price for the limit sell order (1% above purchase price)
            target_price = buy_order['price'] * 1.01
            sell_order = place_limit_sell_order(symbol, btc_amount, target_price)
            print(f"Limit sell order placed at {target_price}: {sell_order}")

        # Wait for a certain amount of time before checking again (e.g., 60 seconds)
        time.sleep(60)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        time.sleep(60)
