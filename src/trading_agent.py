from order import Order
import random
import time
from datetime import datetime

'''
Generates and submits orders at a specified rate for multiple instruments.
'''
class TradingAgent:
    def __init__(self, agent_id, order_rate, symbols):
        self.agent_id = agent_id
        self.order_rate = order_rate
        self.symbols = symbols
        self.running = False
        self.next_order_id = 1

    def run(self, matching_engines):
        self.running = True
        while self.running:
            time.sleep(1 / self.order_rate)
            symbol = random.choice(self.symbols)
            # Specifying price interval
            price = round(random.uniform(90.0, 210.0), 1)  # Ensure price precision to 0.1
            # Specifying amount interval
            amount = random.randint(1, 110)
            order_type = random.choice(['BUY', 'SELL'])
            timestamp = datetime.now().isoformat(timespec='seconds')
            order = Order(self.next_order_id, self.agent_id, symbol, price, amount, order_type, timestamp)
            self.next_order_id += 1
            matching_engines[symbol].submit_order(order)

    def stop(self):
        self.running = False