import argparse
from config import get_client, logger
from utils import validate_symbol, validate_positive_number
from market_orders import place_market_order
from limit_orders import place_limit_order

def main():
    parser = argparse.ArgumentParser(description="Binance Futures CLI Bot (Testnet by default)")
    parser.add_argument("--live", action="store_true", help="Use live trading instead of testnet")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # Market order parser
    mkt = sub.add_parser("market", help="Place a market order")
    mkt.add_argument("--symbol", required=True, help="Symbol, e.g. BTCUSDT")
    mkt.add_argument("--side", required=True, choices=["BUY", "SELL"], help="BUY or SELL")
    mkt.add_argument("--qty", required=True, help="Quantity (contract units)")

    # Limit order parser
    lim = sub.add_parser("limit", help="Place a limit order")
    lim.add_argument("--symbol", required=True, help="Symbol, e.g. BTCUSDT")
    lim.add_argument("--side", required=True, choices=["BUY", "SELL"], help="BUY or SELL")
    lim.add_argument("--qty", required=True, help="Quantity (contract units)")
    lim.add_argument("--price", required=True, help="Limit price")

    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        qty = validate_positive_number(args.qty, "qty")
        client = get_client(testnet=not args.live)
    except Exception as e:
        logger.error(f"Setup/validation error: {e}")
        print("Error:", e)
        return

    if args.cmd == "market":
        place_market_order(client, symbol, args.side, qty)
    elif args.cmd == "limit":
        try:
            price = validate_positive_number(args.price, "price")
        except Exception as e:
            logger.error(f"Price validation error: {e}")
            print("Error:", e)
            return
        place_limit_order(client, symbol, args.side, qty, price)

if __name__ == "__main__":
    main()
