import os
import logging
from dotenv import load_dotenv
from binance.um_futures import UMFutures

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Logger setup
logger = logging.getLogger("bot")
logger.setLevel(logging.DEBUG)
fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
sh = logging.StreamHandler()
sh.setFormatter(fmt)
fh = logging.FileHandler("bot.log")
fh.setFormatter(fmt)
logger.addHandler(sh)
logger.addHandler(fh)

def get_client(testnet=True):
    if not API_KEY or not API_SECRET:
        logger.error("API key/secret not set in .env file.")
        raise SystemExit("Set BINANCE_API_KEY and BINANCE_API_SECRET in .env")

    base_url = "https://testnet.binancefuture.com"
    try:
        client = UMFutures(key=API_KEY, secret=API_SECRET, base_url=base_url, timeout=10)
        server_time = client.time()
        logger.info(f"Binance Futures client created. Testnet={testnet}, Server Time={server_time}")
        return client
    except Exception as e:
        logger.error(f"Failed to create Binance Futures client: {e}")
        raise

