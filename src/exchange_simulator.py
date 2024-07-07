from matching_engine import MatchingEngine
from trading_agent import TradingAgent

import time
import threading

'''
Simulator that models the interaction between the matching engines and trading agents.
'''
class ExchangeSimulator:
    def __init__(self):
        self.matching_engines = {}
        self.trading_agents = []
        self.running = False
        self.callbacks = {
            'order_accepted': None,
            'order_rejected': None,
            'trade_executed': None
        }

    def add_matching_engine(self, symbol):
        self.matching_engines[symbol] = MatchingEngine(symbol, self)

    def add_trading_agent(self, agent_id, order_rate, symbols):
        agent = TradingAgent(agent_id, order_rate, symbols)
        self.trading_agents.append(agent)

    def register_callback(self, event, callback):
        if event in self.callbacks:
            self.callbacks[event] = callback

    def run(self, duration):
        self.running = True
        threads = []
        for agent in self.trading_agents:
            t = threading.Thread(target=agent.run, args=(self.matching_engines,))
            t.daemon = True
            threads.append(t)
            t.start()

        time.sleep(duration)
        self.stop()

        for t in threads:
            t.join()

    def stop(self):
        self.running = False
        for agent in self.trading_agents:
            agent.stop()

    def on_order_accepted(self, order):
        if self.callbacks['order_accepted']:
            self.callbacks['order_accepted'](order)

    def on_order_rejected(self, order):
        if self.callbacks['order_rejected']:
            self.callbacks['order_rejected'](order)

    def on_trade_executed(self, trade):
        if self.callbacks['trade_executed']:
            self.callbacks['trade_executed'](trade)

    def get_order_book(self, symbol):
        if symbol in self.matching_engines:
            return self.matching_engines[symbol].get_order_book()
        return None