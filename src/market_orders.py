from binance.error import ClientError
from config import logger

def place_market_order(client, symbol: str, side: str, quantity):
    logger.info(f"Placing MARKET order: {symbol} {side} {quantity}")
    try:
        resp = client.new_order(symbol=symbol, side=side, type="MARKET", quantity=float(quantity))
        logger.info(f"Order response: {resp}")
        print("ORDER RESPONSE:", resp)
    except ClientError as e:
        logger.error(f"API error placing market order: {e}")
        print("API error:", e)
