# 🐍 Binance USDT-M Futures CLI Trading Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Binance](https://img.shields.io/badge/Binance-Futures-yellow?style=for-the-badge&logo=binance&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

*A powerful Command-Line Interface (CLI) bot for **Binance USDT-M Futures** built with Python*

[Features](#-features) • [Installation](#️-installation--setup) • [Usage](#-usage) • [Documentation](#-documentation)

</div>

---

## 🌟 Overview

A comprehensive **CLI trading bot** for Binance USDT-M Futures with robust logging, input validation, and modular architecture. Designed for both beginners and advanced traders who prefer command-line interfaces.

> ⚠️ **Safety First** – This bot runs on Binance Futures **Testnet** by default to prevent real losses during development and testing.

---

## ✨ Features

<table>
<tr>
<td>

### 📊 **Trading Capabilities**
- ✅ Market Orders
- ✅ Limit Orders
- ✅ Real-time order execution
- ✅ Position management

</td>
<td>

### 🔧 **Technical Features**
- ✅ Comprehensive logging system
- ✅ Input validation & error handling
- ✅ Modular code architecture
- ✅ CLI argument parsing

</td>
</tr>
</table>

### 🛡️ **Safety & Reliability**
- **Testnet Integration** – Safe testing environment
- **Error Handling** – Graceful failure management
- **Logging System** – Complete audit trail
- **Validation Checks** – Symbol and price filter validation

---

## 📂 Project Structure

```
Zaid_Binance_Bot/
│
├── 📁 src/
│   ├── 🚀 cli.py                # CLI entry point
│   ├── ⚙️  config.py             # Environment & client setup
│   ├── 📈 market_orders.py      # Market order functionality
│   ├── 📊 limit_orders.py       # Limit order functionality
│   └── 🛠️  utils.py              # Helper functions (e.g., price filters)
│
├── 🔐 .env                    # Your API keys (never commit this)
├── 📋 requirements.txt        # Python dependencies
├── 📖 README.md               # Project documentation
└── 📝 bot.log                 # Auto-generated log file
```

---

## ⚙️ Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/zaidcodes72/zaid_binance_bot.git
cd Zaid_Binance_Bot
```

### 2️⃣ **Create Virtual Environment**
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate    # 🐧 Linux/Mac
# OR
.venv\Scripts\activate       # 🪟 Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Setup Environment Variables**
Create a `.env` file in the root directory:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

> 🔑 **Get your Testnet keys** from [Binance Futures Testnet](https://testnet.binancefuture.com)

---

## 🚀 Usage

Run CLI commands from the project root directory:

### 📈 **Place a Market Order**
```bash
python src/cli.py market --symbol BTCUSDT --side BUY --qty 0.01
```

### 📊 **Place a Limit Order**
```bash
python src/cli.py limit --symbol BTCUSDT --side SELL --qty 0.01 --price 90000
```

### 📋 **Command Arguments**

| Parameter | Description | Example | Required |
|-----------|-------------|---------|----------|
| `--symbol` | Trading pair | `BTCUSDT` | ✅ |
| `--side` | Order direction | `BUY` / `SELL` | ✅ |
| `--qty` | Quantity to trade | `0.01` | ✅ |
| `--price` | Price (limit orders only) | `90000` | ⚠️ Limit only |

### 💡 **Usage Examples**

<details>
<summary><strong>📈 Market Order Examples</strong></summary>

```bash
# Buy 0.01 BTC at market price
python src/cli.py market --symbol BTCUSDT --side BUY --qty 0.01

# Sell 0.005 ETH at market price
python src/cli.py market --symbol ETHUSDT --side SELL --qty 0.005

# Buy 1000 DOGE at market price
python src/cli.py market --symbol DOGEUSDT --side BUY --qty 1000
```
</details>

<details>
<summary><strong>📊 Limit Order Examples</strong></summary>

```bash
# Sell 0.01 BTC at $90,000
python src/cli.py limit --symbol BTCUSDT --side SELL --qty 0.01 --price 90000

# Buy 0.1 ETH at $3,200
python src/cli.py limit --symbol ETHUSDT --side BUY --qty 0.1 --price 3200

# Sell 5000 DOGE at $0.08
python src/cli.py limit --symbol DOGEUSDT --side SELL --qty 5000 --price 0.08
```
</details>

---

## 📜 Logging

The bot maintains comprehensive logs stored in `bot.log` and displays real-time information in the terminal.

### 📊 **Log Categories**
- **INFO** - Successful operations and status updates
- **ERROR** - API errors and failed operations
- **DEBUG** - Detailed execution information

### 📝 **Sample Log Output**
```log
2025-08-09 17:04:52,432 - INFO - Binance Futures client created. Testnet=True
2025-08-09 17:04:52,434 - INFO - Placing LIMIT order: BTCUSDT SELL 0.01 @ 90000
2025-08-09 17:04:53,255 - ERROR - API error: Price less than min price.
2025-08-09 17:04:54,100 - INFO - Order placed successfully: Order ID 12345678
```

---

## 🔧 Configuration

### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `BINANCE_API_KEY` | Your Binance API key | ✅ |
| `BINANCE_API_SECRET` | Your Binance API secret | ✅ |

### 🏗️ **Architecture Benefits**
- **Modular Design** - Easy to extend and maintain
- **Error Handling** - Robust error management
- **Logging Integration** - Complete operation tracking
- **CLI Interface** - Simple command-line usage

---

## ⚠️ Disclaimer

This software is for **educational and testing purposes only**. Always test on **Binance Testnet** before considering any real trading. Cryptocurrency trading involves significant risk and can result in loss of funds.

---

## 📚 References

- 📖 [Binance Futures API Documentation](https://binance-docs.github.io/apidocs/futures/en/)
- 🧪 [Binance Futures Testnet](https://testnet.binancefuture.com)
- 🐍 [Python Binance Documentation](https://python-binance.readthedocs.io/)

---

<div align="center">

### 🌟 **Star this repository if you found it helpful!** 🌟

Made with ❤️ by [zaidcodes72](https://github.com/zaidcodes72)

</div>