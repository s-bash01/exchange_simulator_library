'''
Represents a Trade executed on the exchange simulator
'''
class Trade:
    def __init__(self, trade_id, symbol, price, amount, buy_order, sell_order):
        self.trade_id = trade_id
        self.symbol = symbol
        self.price = price
        self.amount = amount
        self.buy_order = buy_order
        self.sell_order = sell_order

    def __repr__(self):
        # Provides a string representation of the Trade object for logging and debugging purposes.
        return f"Trade(id={self.trade_id}, symbol='{self.symbol}', price={self.price}, amount={self.amount})"
