# Crypto Day Trading

This repository provides tools for crypto day trading, including `test.py` for testing market data and `make_order.py` for executing trades. Follow the instructions below to set up the environment and run the scripts successfully.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setting up the .env File](#setting-up-the-env-file)
- [Running the Code](#running-the-code)

## Prerequisites

Before using this repository, ensure you have the following installed:

- Python 3.8 or higher
- `pip` (Python package installer)

You will also need API keys from your preferred crypto trading platform (e.g., Binance, Coinbase Pro, etc.) for the scripts to interact with the exchange.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MinasAcademy/crypto-day-trading.git
   cd crypto-day-trading
   ```

2. **Set up a Python virtual environment:**

    It's recommended to use a virtual environment to manage dependencies. You can set one up with the following commands:

    For Windows:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    For macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies:** 

    After activating the virtual environment, install the dependencies listed in the requirements.txt file:

    ```bash
    pip install -r requirements.txt
    ```

## Setting up the .env File

The scripts require API keys to interact with the crypto exchange. You will need to create a .env file in the root of the project and add your API keys and secrets.

1. **Create a .env file in the root directory:**

    ```bash
    touch .env
    ```
2. **Add your API keys to the .env file.**

    The format should be as follows:

    ```makefile
    API_KEY=your_api_key_here
    API_SECRET=your_api_secret_here
    ```
    Replace your_api_key_here and your_api_secret_here with the actual API key and secret obtained from your exchange account.

## Running the Code
1. **Test the market data using test.py:**

    This script is used to retrieve and test market data from the crypto exchange.

    ```bash
    python test.py
    ```
    This will run the script, and you should see market data output if the API keys are correctly set up.

2. **Place an order using make_order.py:**

    This script allows you to place a crypto order (buy or sell) on the exchange.

    ```bash
    python make_order.py
    ```
    The script will execute an order based on the logic implemented in make_order.py.

## Troubleshooting
- If you encounter issues with API keys, ensure that they are correctly entered in the .env file and that your exchange account has API trading enabled.
- Make sure to activate the virtual environment before running the scripts.

