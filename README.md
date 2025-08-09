# 🐍 Binance USDT-M Futures CLI Trading Bot

A Command-Line Interface (CLI) bot for **Binance USDT-M Futures** built in Python.  
Supports **Market Orders** and **Limit Orders** with **robust logging**, **input validation**, and **modular code structure** for easy maintainability.  

> ⚠️ **Testnet Only** – This bot is configured to run on Binance Futures **Testnet** to prevent real losses.

---

## 📌 Features

- **Order Types**
  - ✅ Market Orders
  - ✅ Limit Orders
- **Logging**
  - Console + File logging for debugging and trade tracking.
- **Validation**
  - Basic checks for API keys, order inputs, and symbol price filters.
- **Modular Structure**
  - Separate files for market and limit orders for maintainability.
- **CLI Support**
  - Simple commands to execute trades directly from the terminal.

---

## 📂 Project Structure

Zaid_Binance_Bot/
│
├── src/
│ ├── cli.py                # CLI entry point
│ ├── config.py             # Environment & client setup
│ ├── market_orders.py      # Market order functionality
│ ├── limit_orders.py       # Limit order functionality
│ ├── utils.py              # Helper functions (e.g., price filters)
│
├── .env                    # Your API keys (never commit this)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── bot.log                 # Auto-generated log file

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/zaidcodes72/zaid_binance_bot.git
cd Zaid_Binance_Bot

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\activate       # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup .env File
Create a .env file in the root directory:

BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
🔑 Get your Testnet keys from Binance Futures Testnet.

🚀 Usage
Run CLI commands from the project root:

Place a Market Order -
python src/cli.py market --symbol BTCUSDT --side BUY --qty 0.01

Place a Limit Order -
python src/cli.py limit --symbol BTCUSDT --side SELL --qty 0.01 --price 90000

Arguments:
Parameter	Description	                    Example
--symbol	Trading pair	                BTCUSDT
--side	    BUY or SELL	BUY                 BUY
--qty	    Quantity to trade	            0.01
--price	    Price (only for limit orders)	90000

📜 Logging
Logs are stored in bot.log and also displayed in the terminal.

Includes:

API connection status
Order requests & responses
Error messages

Example log entry:

2025-08-09 17:04:52,432 - INFO - Binance Futures client created. Testnet=True
2025-08-09 17:04:52,434 - INFO - Placing LIMIT order: BTCUSDT SELL 0.01 @ 90000
2025-08-09 17:04:53,255 - ERROR - API error: Price less than min price.

📖 References
Binance Futures API Documentation

Binance Futures Testnet