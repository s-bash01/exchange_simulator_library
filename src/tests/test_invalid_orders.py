import unittest
from exchange_simulator import ExchangeSimulator
from order import Order
import time

'''
Functional test to check if invalid orders based on Price and Amount is handled
'''

class TestInvalidOrders(unittest.TestCase):

    def initialize_simulator(self):
        self.simulator = ExchangeSimulator()
        self.simulator.add_matching_engine("TSLA")
        self.simulator.add_trading_agent("agent_1", 1, ["TSLA"])

    def test_invalid_price(self):
        self.initialize_simulator()
        invalid_order = Order(1, 1, "TSLA", 400, 20, 'BUY', time.time())
        self.simulator.matching_engines["TSLA"].submit_order(invalid_order)
        order_book = self.simulator.get_order_book("TSLA")
        self.assertEqual(len(order_book), 0)  # Order should be rejected

    def test_invalid_amount(self):
        self.initialize_simulator()
        invalid_order = Order(2, 1, "TSLA", 125, 300, 'BUY', time.time())
        self.simulator.matching_engines["TSLA"].submit_order(invalid_order)
        order_book = self.simulator.get_order_book("TSLA")
        self.assertEqual(len(order_book), 0)  # Order should be rejected

if __name__ == '__main__':
    unittest.main()