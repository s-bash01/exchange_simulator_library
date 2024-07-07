from order import Order
from trade import Trade
import threading
from queue import PriorityQueue
import time

'''
Manages the order book and matches incoming orders based on price-time priority.
'''
class MatchingEngine:
    def __init__(self, symbol, simulator):
        self.symbol = symbol
        self.simulator = simulator
        self.buy_orders = PriorityQueue()
        self.sell_orders = PriorityQueue()
        self.lock = threading.Lock()
        self.next_trade_id = 1

    def submit_order(self, order):
        with self.lock:
            order.price = round(order.price, 1)  # Ensure price precision to 0.1
            # Reject invalid orders based on price and amount
            if order.price < 100 or order.price > 200 or order.amount > 100:
                self.simulator.on_order_rejected(order)
                return
            if order.symbol != self.symbol:
                self.simulator.on_order_rejected(order)
                return

            if order.type == 'BUY':
                self.buy_orders.put((-order.price, order))
            elif order.type == 'SELL':
                self.sell_orders.put((order.price, order))

            # Show an order is accepted
            self.simulator.on_order_accepted(order)
            
            # Schedule order cancellation after 5 seconds
            threading.Timer(5, self.cancel_order, [order]).start()
            
            self.match_orders()

    def match_orders(self):
        while not self.buy_orders.empty() and not self.sell_orders.empty():
            buy_order = self.buy_orders.queue[0][1]
            sell_order = self.sell_orders.queue[0][1]

            if buy_order.price >= sell_order.price:
                trade_amount = min(buy_order.amount, sell_order.amount)
                trade_price = sell_order.price

                trade = Trade(self.next_trade_id, buy_order.symbol, trade_price, trade_amount, buy_order, sell_order)
                self.next_trade_id += 1
                self.simulator.on_trade_executed(trade)

                buy_order.amount -= trade_amount
                sell_order.amount -= trade_amount

                if buy_order.amount == 0:
                    self.buy_orders.get()
                if sell_order.amount == 0:
                    self.sell_orders.get()
            else:
                break

    def get_order_book(self):
        with self.lock:
            return [order[1] for order in list(self.buy_orders.queue)] + [order[1] for order in list(self.sell_orders.queue)]

    def cancel_order(self, order):
        with self.lock:
            if order.type == 'BUY':
                self.buy_orders.queue = [item for item in self.buy_orders.queue if item[1] != order]
                self.buy_orders.queue.sort(reverse=True)
            elif order.type == 'SELL':
                self.sell_orders.queue = [item for item in self.sell_orders.queue if item[1] != order]
                self.sell_orders.queue.sort()
            self.match_orders()
