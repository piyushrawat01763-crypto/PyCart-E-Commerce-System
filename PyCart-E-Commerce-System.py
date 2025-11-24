import json
import os
import time

# --- Configuration ---
DATA_FILE = 'shopping_data.json'

class Product:
    """Represents a product in the store's inventory."""
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        """String representation for display."""
        return f"({self.product_id}) {self.name} - ${self.price:.2f} (Stock: {self.stock})"

    def to_dict(self):
        """Converts the product object to a dictionary for saving."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock
        }

# Global store state
inventory = {}  # {product_id: Product object}
cart = {}       # {product_id: quantity}

def load_data():
    """Loads inventory and cart data from a JSON file, or initializes defaults."""
    global inventory, cart
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                
            # Load Inventory
            inventory = {
                pid: Product(**item)
                for pid, item in data.get('inventory', {}).items()
            }
            # Load Cart
            cart = {
                pid: quantity
                for pid, quantity in data.get('cart', {}).items()
            }
            print("🛍️ Data loaded successfully.")
            
        except (IOError, json.JSONDecodeError):
            print("⚠️ Error loading data. Starting with default inventory.")
            initialize_default_inventory()
    else:
        print("📁 Data file not found. Initializing default inventory.")
        initialize_default_inventory()

def initialize_default_inventory():
    """Sets up a default inventory if no data file exists."""
    global inventory
    inventory = {
        '101': Product('101', 'Python Programming Book', 39.99, 15),
        '102': Product('102', 'Mechanical Keyboard', 85.00, 8),
        '103': Product('103', 'LED Monitor 27"', 199.99, 5),
        '104': Product('104', 'Wireless Mouse', 24.50, 20),
        '105': Product('105', 'USB-C Cable', 9.00, 50),
    }
    # Initialize an empty cart as well
    global cart
    cart = {}

def save_data():
    """Saves the current inventory and cart state to the JSON file."""
    data = {
        'inventory': {pid: prod.to_dict() for pid, prod in inventory.items()},
        'cart': cart
    }
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        print("💾 State saved.")
    except IOError:
        print("❌ Error saving data.")

def display_inventory():
    """Prints the available products."""
    print("\n" + "="*40)
    print("           AVAILABLE PRODUCTS")
    print("="*40)
    if not inventory:
        print("Inventory is currently empty.")
        return

    for prod in inventory.values():
        if prod.stock > 0:
            print(prod)
    print("="*40)

def add_to_cart():
    """Handles adding a specified quantity of a product to the cart."""
    display_inventory()
    
    product_id = input("Enter Product ID to add (e.g., 101): ").strip()
    
    if product_id not in inventory:
        print(f"🚫 Error: Product ID '{product_id}' not found.")
        return

    product = inventory[product_id]
    
    try:
        quantity = int(input(f"Enter quantity of '{product.name}' to add: "))
        if quantity <= 0:
            print("🚫 Quantity must be a positive number.")
            return
    except ValueError:
        print("🚫 Invalid quantity input. Please enter a number.")
        return

    current_cart_qty = cart.get(product_id, 0)
    
    if (current_cart_qty + quantity) > product.stock:
        print(f"⛔ Not enough stock! Available stock: {product.stock}. "
              f"You already have {current_cart_qty} in cart.")
    else:
        # Update cart quantity (add new or increase existing)
        cart[product_id] = current_cart_qty + quantity
        print(f"✅ Added {quantity} x {product.name} to cart.")

def view_cart():
    """Displays the current contents and total cost of the shopping cart."""
    print("\n" + "="*40)
    print("           SHOPPING CART")
    print("="*40)
    if not cart:
        print("Your cart is empty.")
        print("="*40)
        return

    total_cost = 0.0
    
    for product_id, quantity in cart.items():
        if product_id in inventory:
            product = inventory[product_id]
            line_total = product.price * quantity
            total_cost += line_total
            print(f"{product.name.ljust(25)} x {str(quantity).ljust(2)} @ ${product.price:.2f} = ${line_total:.2f}")
        else:
            # Handle case where product was deleted from inventory but is still in cart
            print(f"[Product ID: {product_id}] - Item unavailable (REMOVE from cart)")

    print("-" * 40)
    print(f"Subtotal: {' '*18} ${total_cost:.2f}")
    print("="*40)

def checkout():
    """Finalizes the purchase, updates inventory, and clears the cart."""
    view_cart()

    if not cart:
        print("Cannot checkout. Your cart is empty.")
        return

    confirm = input("Proceed to payment? (yes/no): ").strip().lower()

    if confirm == 'yes':
        # 1. Update inventory stock
        for product_id, quantity in cart.items():
            if product_id in inventory:
                inventory[product_id].stock -= quantity
        
        # 2. Clear the cart
        cart.clear()
        
        print("\n" + "*"*40)
        print("🎉 ORDER CONFIRMED! Thank you for your purchase!")
        print("Your cart has been cleared. Inventory updated.")
        print("*"*40)
        
        # Save the updated inventory state
        save_data()
        time.sleep(2)
        
    else:
        print("Checkout cancelled.")

def main_menu():
    """Displays the main menu options."""
    print("\n" + "#"*40)
    print("       WELCOME TO THE PYTHON STORE")
    print("#"*40)
    print("1. Browse Products (View Inventory)")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Save & Exit")
    print("Q. Quick Exit (without saving)")
    print("#"*40)

def run_app():
    """The main application loop."""
    load_data()

    while True:
        main_menu()
        choice = input("Enter your choice (1-5, Q): ").strip().upper()

        if choice == '1':
            display_inventory()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            checkout()
        elif choice == '5':
            save_data()
            print("Goodbye!")
            break
        elif choice == 'Q':
            print("Exiting without saving changes. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")
        
        # Pause briefly before returning to the main menu
        if choice in ('1', '2', '3'):
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    run_app()
