from customer_data_store import customer_data
from validation import is_valid_email, is_valid_phone
from datetime import datetime

def display_customers():
    print("\nAll Customers:")
    for customer in customer_data:
        print(f"{customer['id']}: {customer['name']} ({customer['email']})")

def add_customer():
    try:
        new_id = max([c["id"] for c in customer_data]) + 1
    except ValueError:
        new_id = 1

    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    address = input("Enter address: ")
    membership = input("Enter membership (Gold/Silver/Bronze): ")
    join_date = input("Enter join date (YYYY-MM-DD): ")
    balance = float(input("Enter balance: "))

    if not is_valid_email(email):
        print("Invalid email.")
        return
    if not is_valid_phone(phone):
        print("Invalid phone.")
        return
    try:
        datetime.strptime(join_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    customer_data.append({
        "id": new_id,
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "membership": membership,
        "join_date": join_date,
        "balance": balance
    })
    print("Customer added successfully.")

def amend_customer():
    try:
        cid = int(input("Enter customer ID to amend: "))
        customer = next(c for c in customer_data if c["id"] == cid)
        customer["name"] = input("Enter new name: ") or customer["name"]
        print("Customer updated.")
    except:
        print("Customer not found.")

def delete_customer():
    try:
        cid = int(input("Enter customer ID to delete: "))
        customer_data[:] = [c for c in customer_data if c["id"] != cid]
        print("Customer deleted.")
    except:
        print("Customer not found.")

def view_customer_by_id():
    try:
        cid = int(input("Enter customer ID to view: "))
        cust = next(c for c in customer_data if c["id"] == cid)
        for k, v in cust.items():
            print(f"{k.capitalize()}: {v}")
    except:
        print("Customer not found.")