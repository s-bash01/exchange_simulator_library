import unittest
from exchange_simulator import ExchangeSimulator
from order import Order
import time

'''
Functional test to check the handling of order matching based on requirements such as;
  - Incoming buy (bid) orders are crossed against existing sell (offer) orders, and vice versa.
  - A match occurs if and only if the buy price is equal or greater than the sell price of the crossed order.
  - A match results in an executed trade, and the matched amount is reduced from the amount remaining on both of the
    crossed orders. If an order has no amount remaining, it is removed from the order book.
  - Use price-time priority. That means that if two orders are at the same price, preference is giving to matching
    the oldest order first.
'''

class TestOrderMatching(unittest.TestCase):

    def initialize_simulator(self):
        self.simulator = ExchangeSimulator()
        self.simulator.add_matching_engine("TSLA")
        self.simulator.add_trading_agent("agent_1", 1, ["TSLA"])
        self.simulator.add_trading_agent("agent_2", 1, ["TSLA"])

    def test_order_matching(self):
        self.initialize_simulator()
        buy_order = Order(1, 1, "TSLA", 150, 20, 'BUY', time.time()) # Buy price greater than sell price
        sell_order = Order(2, 2, "TSLA", 125, 20, 'SELL', time.time()) 
        self.simulator.matching_engines["TSLA"].submit_order(buy_order)
        self.simulator.matching_engines["TSLA"].submit_order(sell_order)
        order_book = self.simulator.get_order_book("TSLA")
        self.assertEqual(len(order_book), 0)  # Order is matched and removed since no more amount left


    def test_order_priority(self):
        self.initialize_simulator()
        sell_order = Order(1, 1, "TSLA", 125, 20, 'SELL', time.time()) # Sell order first this time
        buy_order1 = Order(2, 2, "TSLA", 125, 20, 'BUY', time.time()) # Buy price of first order equal to sell price
        time.sleep(0.02)  # Ensure a slight delay for the second order
        buy_order2 = Order(3, 3, "TSLA", 125, 20, 'BUY', time.time())

        self.simulator.matching_engines["TSLA"].submit_order(buy_order1)
        self.simulator.matching_engines["TSLA"].submit_order(buy_order2)
        self.simulator.matching_engines["TSLA"].submit_order(sell_order)

        # Since buy_order1 was placed first, it should be matched with sell_order
        self.simulator.matching_engines["TSLA"].match_orders()
        order_book = self.simulator.get_order_book("TSLA")
        self.assertEqual(order_book[0].order_id, buy_order2.order_id)  # buy_order2 should remain in the order book


if __name__ == '__main__':
    unittest.main()