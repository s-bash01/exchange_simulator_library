from datetime import datetime

'''
Represents an Order placed on the exchange simulator
'''
class Order:
    def __init__(self, order_id, agent_id, symbol, price, amount, order_type, timestamp):
        self.order_id = order_id
        self.agent_id = agent_id
        self.type = order_type # order direction - BUY/SELL
        self.symbol = symbol
        self.price = price
        self.amount = amount
        self.timestamp = timestamp if timestamp else datetime.now.isoformat(timespec='seconds')

    def __repr__(self):
        # Provides a string representation of the Trade object for logging and debugging purposes.
        return f"Order(id={self.order_id}, agent_id={self.agent_id}, symbol='{self.symbol}', price={self.price}, amount={self.amount}, type={self.type}, timestamp={self.timestamp})"

    def __lt__(self, other):
        # Compares two orders, giving priority based on price and timestamp.
        if self.price == other.price:
            return self.timestamp < other.timestamp
        return self.price < other.price if self.type == 'SELL' else self.price > other.price
