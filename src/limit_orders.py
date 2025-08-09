from binance.error import ClientError
from config import logger

def place_limit_order(client, symbol: str, side: str, quantity, price):
    logger.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")
    try:
        resp = client.new_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=float(quantity),
            price=str(price)
        )
        logger.info(f"Order response: {resp}")
        print("ORDER RESPONSE:", resp)
    except ClientError as e:
        logger.error(f"API error placing limit order: {e}")
        print("API error:", e)
