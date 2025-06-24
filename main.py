from ui import display_main_menu
from customer_ops import (
    display_customers,
    add_customer,
    amend_customer,
    delete_customer,
    view_customer_by_id
)

def main():
    while True:
        choice = display_main_menu()
        if choice == "1":
            display_customers()
        elif choice == "2":
            add_customer()
        elif choice == "3":
            amend_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "5":
            view_customer_by_id()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()