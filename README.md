# Exchange Simulator Library

The Exchange Simulator Library models interactions between trading agents and matching engines in a real-time trading environment. This library provides a flexible platform for simulating trading activities, allowing users to define custom trading agents and matching engines, register event callbacks, and observe order and trade activities.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Components](#components)
  - [Matching Engine](#matching-engine)
  - [Trading Agent](#trading-agent)
- [Public Interface](#public-interface)
- [Functional Tests](#functional-tests)

## Features

- Real-time simulation with realistic delays and timing.
- Customizable matching engines and trading agents.
- Event callbacks for order acceptance, rejection, and trade execution.
- Efficient order matching using price-time priority.
- Comprehensive tests for functionality validation.

## Installation

Download the repository and navigate to the project directory:

Open the folder then change directory to src

`cd src`


## Usage

Run the simulation with predefined settings by executing the main.py file:

`python -m main`

This sets up the simulation, registers event callbacks, adds trading agents and matching engines, and runs the simulation for a specified duration.

## Components

### Matching Engine

- Maintains an order book and matches incoming orders with existing ones.
- Uses a Central Limit Order Book (CLOB) and prioritizes orders based on price-time priority.
- An order is accepted unless the price is outside of the valid trading range [100.0, 200.0], or the amount is larger than 100.
- Rejected orders are not placed in the order book.
- Orders are cancelled if not fully matched within the specified time frame of 5 seconds and removed from order book simulating a "Good Till Time" order type.

### Trading Agent

- Generates and submits orders over time to matching engines.
- Submits orders for multiple instruments.
- Generates orders as independent random events with a specified average rate.
- Randomizes properties of each order, including buy/sell direction, price within interval [90.0, 210.0] with precision of 0.1,and amount, within interval [1, 110]


## Public Interface

The public interface is provided in the main.py file. This file demonstrates how to:
- Define and configure matching engines and trading agents.
- Register custom event callbacks.
- Run the simulation for a specified duration.
- Retrieve and display the order book.

## Functional Tests

The Functional Tests are located in the tests directory and are run using the built-in unittest framework. 

To run all tests Ensure you are in the `src` directory then run the following command:

`python -m unittest discover -s tests`

To run a single test run the following command:

`python -m unittest tests.<test_file_name>` for example:

`python -m unittest tests.test_invalid_order`


### Functional Tests Structure

- test_invalid_orders.py: Functional test to check if invalid orders based on Price and Amount is handled.
- test_order_cancellation.py: Functional test to check if order cancellation after 5 seconds is handled.
- test_order_matching.py: Functional test to check the handling of order matching based on requirements.
- test_single_order.py: Functional tests to check submission and processing of a single orders.
- test_stress_testing.py: Functional Test to check if the simulator under high load and stress conditions.