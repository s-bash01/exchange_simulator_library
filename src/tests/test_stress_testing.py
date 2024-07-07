import unittest
from exchange_simulator import ExchangeSimulator
import time

'''
Functional Test to check if the simulator under high load and stress conditions
'''
class TestStressTesting(unittest.TestCase):

    def initialize_simulator(self):
        self.simulator = ExchangeSimulator()
        self.simulator.add_matching_engine("TSLA")
        self.simulator.add_matching_engine("NFLX")
        self.simulator.add_trading_agent("agent_1", 100, ["TSLA", "NFLX"])  # High order rate
        self.simulator.add_trading_agent("agent_2", 100, ["TSLA", "NFLX"])  # High order rate
    
    def test_stress_testing(self):
        self.initialize_simulator()
        self.simulator.run(10)  # Run the simulation for 10 seconds
        tsla_order_book = self.simulator.get_order_book("TSLA")
        nflx_order_book = self.simulator.get_order_book("NFLX")
        self.assertTrue(len(tsla_order_book) > 0)  # Order book should contain many orders
        self.assertTrue(len(nflx_order_book) > 0)  # Order book should contain many orders
        
if __name__ == '__main__':
    unittest.main()
