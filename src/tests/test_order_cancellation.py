import unittest
from exchange_simulator import ExchangeSimulator
from order import Order
import time

'''
Functional test to check if order cancellation after 5 seconds is handled
'''
class TestOrderCancellation(unittest.TestCase):

    def initialize_simulator(self):
        self.simulator = ExchangeSimulator()
        self.simulator.add_matching_engine("TSLA")
        self.simulator.add_trading_agent("agent_1", 1, ["TSLA"])

    def test_order_cancellation(self):
        self.initialize_simulator()
        order = Order(1, 1, "TSLA", 125, 10, 'BUY', time.time())
        self.simulator.matching_engines["TSLA"].submit_order(order)
        time.sleep(6)  # Wait to ensure the order is canceled
        order_book = self.simulator.get_order_book("TSLA")
        self.assertEqual(len(order_book), 0)  # Order should be canceled

if __name__ == '__main__':
    unittest.main()