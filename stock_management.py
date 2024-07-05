import tkinter as tk
from tkinter import messagebox

# Initialize an empty dictionary to store stock items
stock = {}

# Function to add a new item to the stock
def add_item():
    item_name = item_entry.get()
    quantity = int(quantity_entry.get())
    
    if item_name and quantity > 0:
        stock[item_name] = quantity
        update_status(f"{item_name} added to stock with quantity {quantity}.")
    else:
        messagebox.showwarning("Error", "Please enter valid item name and quantity.")

    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

# Function to display all items in the stock
def display_stock():
    if not stock:
        update_status("Stock is empty.")
    else:
        stock_info = "Current Stock:\n"
        for item, quantity in stock.items():
            stock_info += f"{item}: {quantity}\n"
        update_status(stock_info)

# Function to update the quantity of an existing item
def update_item():
    item_name = item_entry.get()
    if item_name in stock:
        new_quantity = int(quantity_entry.get())
        stock[item_name] = new_quantity
        update_status(f"Quantity updated for {item_name}.")
    else:
        messagebox.showwarning("Error", f"{item_name} not found in stock.")

    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

# Function to remove an item from the stock
def remove_item():
    item_name = item_entry.get()
    if item_name in stock:
        del stock[item_name]
        update_status(f"{item_name} removed from stock.")
    else:
        messagebox.showwarning("Error", f"{item_name} not found in stock.")

    item_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

# Function to update status label
def update_status(message):
    status_label.config(text=message)

# Main Tkinter application

root = tk.Tk()
root.title("Stock Management System")

# Labels
item_label = tk.Label(root, text="Item:")
item_label.grid(row=0, column=0, padx=10, pady=5)
quantity_label = tk.Label(root, text="Quantity:")
quantity_label.grid(row=1, column=0, padx=10, pady=5)

# Entry fields
global item_entry, quantity_entry
item_entry = tk.Entry(root, width=30)
item_entry.grid(row=0, column=1, padx=10, pady=5)
quantity_entry = tk.Entry(root, width=30)
quantity_entry.grid(row=1, column=1, padx=10, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.grid(row=2, column=0, padx=10, pady=5)
display_button = tk.Button(root, text="Display Stock", command=display_stock)
display_button.grid(row=2, column=1, padx=10, pady=5)
update_button = tk.Button(root, text="Update Quantity", command=update_item)
update_button.grid(row=3, column=0, padx=10, pady=5)
remove_button = tk.Button(root, text="Remove Item", command=remove_item)
remove_button.grid(row=3, column=1, padx=10, pady=5)

# Status label
global status_label
status_label = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E, padx=10, pady=5)

root.mainloop()
