# PyCart-E-Commerce-System
This description covers the interface (CLI), the core functions (browsing, cart, checkout), the key technical implementation (JSON for persistence), and the target audience ...
Python Command Line Store (PyCart)

Project Overview

A Python Command Line Interface (CLI) store application. It features product browsing, stock-aware cart management, and a checkout process that updates inventory. Data persistence is handled using JSON, allowing the store state (inventory and cart) to be saved and loaded across sessions. Ideal for a first-semester project showcasing object-oriented programming (OOP) and file I/O.

Key Features

Browse Inventory: View all available products, including their ID, name, price, and current stock level.

Persistent Data: Uses JSON to save the current inventory and cart state to a file (shopping_data.json) when the user selects "Save & Exit" (Option 5).

Add to Cart: Allows users to add products by ID and specify a quantity.

Stock Validation: Prevents users from adding more items than are currently available in stock.

View Cart: Displays the items currently held, their quantities, and the running total cost.

Checkout: Finalizes the order, deducting purchased quantities from the main inventory and clearing the user's cart.

Technologies & Tools

Tool/Language

Description

Python 3.x

The core programming language used for all logic.

JSON

Used for file persistence to save and load the store's state.

CLI

Command Line Interface is used for user interaction.

Standard Library

Utilizes built-in modules like os, json, and time.

Installation and Setup

This project requires only a standard Python 3 installation. No external packages are necessary.

Prerequisites

Python 3.6 or higher installed on your system.

Steps to Run

Save the Code: Save the provided code into a file named shopping_app.py.

Open Terminal: Navigate to the directory where you saved shopping_app.py.

Execute: Run the application using the Python interpreter:

python shopping_app.py


The application will start, load any existing data, and present the main menu.

Instructions for Testing

To fully test the application, follow these steps:

Start the App: Run python shopping_app.py.

Test Browsing: Select option 1 (Browse Products) and verify the default products are displayed.

Test Adding Items (Valid):

Select option 2.

Enter an ID (e.g., 101) and a quantity (e.g., 2). Verify the success message.

Test Stock Validation (Invalid):

Select option 2.

Attempt to add a quantity that exceeds the remaining stock for any item. Verify the "Not enough stock!" error message.

Test Cart: Select option 3 (View Cart) and confirm the items and the calculated total are correct.

Test Checkout:

Select option 4 (Checkout).

Confirm with yes. Verify the "ORDER CONFIRMED!" message appears.

Test Persistence:

Select option 5 (Save & Exit).

The file shopping_data.json should now exist in the same directory.

Restart the app (python shopping_app.py).

Select option 1 and verify that the stock levels reflect the items purchased during the previous session.
