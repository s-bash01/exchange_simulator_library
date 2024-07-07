import unittest
from exchange_simulator import ExchangeSimulator
from order import Order
import time

'''
Functional tests to check submission and processing of a single order
'''
class TestSingleOrder(unittest.TestCase):

    def initialize_simulator(self):
        self.simulator = ExchangeSimulator()
        self.simulator.add_matching_engine("TSLA")
        self.simulator.add_trading_agent("agent_1", 1, ["TSLA"])

    def test_single_order_submission(self):
        self.initialize_simulator()
        order = Order(1, 1, "TSLA", 140, 15, 'BUY', time.time())
        self.simulator.matching_engines["TSLA"].submit_order(order)
        order_book = self.simulator.get_order_book("TSLA")
        self.assertEqual(len(order_book), 1)  # Order should be in the order book
        
if __name__ == '__main__':
    unittest.main()