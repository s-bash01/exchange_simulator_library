'''
Public interface to run the exchange simulator with registered callbacks.
'''
from exchange_simulator import ExchangeSimulator

def on_order_accepted(order):
    print(f"Order accepted: {repr(order)}")

def on_order_rejected(order):
    print(f"Order rejected: {repr(order)}")

def on_trade_executed(trade):
    print(f"Trade executed: {repr(trade)}")

def run_simulation():
    simulator = ExchangeSimulator()
    
    # Call backs, that are invoked by the simulator when an order is accepted or rejected
    # by the Matching engine or when a trade is executed with the details of that order or trade
    simulator.register_callback('order_accepted', on_order_accepted)
    simulator.register_callback('order_rejected', on_order_rejected)
    simulator.register_callback('trade_executed', on_trade_executed)

    # A Matching engine can be added using the add_matching_engine method
    simulator.add_matching_engine("TSLA")
    simulator.add_matching_engine("NFLX")

    # Trading agents can be added using the add_trading_agent method
    simulator.add_trading_agent("agent_1", 1, ["TSLA", "NFLX"])
    simulator.add_trading_agent("agent_2", 1, ["TSLA", "NFLX"])
    
    # Simulator is run in real-time
    # The duration, in seconds, can be changed by changing the value in the run method below
    simulator.run(8)
    
    for symbol in ["TSLA", "NFLX"]:
        order_book = simulator.get_order_book(symbol)
        if order_book:
            print(f"\nOrder book for {symbol}:")
            for order in order_book:
                print(order)

# Runs Simulator in real-time
if __name__ == "__main__":
    run_simulation()