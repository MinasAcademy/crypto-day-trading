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
