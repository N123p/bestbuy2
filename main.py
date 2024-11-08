from products import Product
from store import Store

product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]

best_buy = Store(product_list)


def list_all_products(store: Store):
    """Displays all products currently available in the store."""
    products = store.get_all_products()
    print("------")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.show()}")
    print("------")


def show_total_amount(store: Store):
    """Displays the total quantity of all items in the store."""
    total_quantity = store.get_total_quantity()
    print(f"Total of {total_quantity} items in store")


def make_order(store: Store):
    """Handles creating an order by prompting user input for product and quantity.

    Raises:
        ValueError: If input quantity is invalid.
    """
    shopping_list = []
    products = store.get_all_products()

    print("------")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.show()}")
    print("------")
    print("When you want to finish the order, enter empty text.")

    while True:
        try:
            product_input = input("Which product # do you want? ")
            if not product_input:
                break

            product_index = int(product_input) - 1
            product = products[product_index]

            quantity_input = input("What amount do you want? ")
            if not quantity_input:
                break

            quantity = int(quantity_input)
            shopping_list.append((product, quantity))
            print("Product added to list!")

        except ValueError:
            print("Invalid input. Please enter a valid product number and quantity.")
        except IndexError:
            print("Invalid product number. Please select a number from the list.")

    try:
        total_cost = store.order(shopping_list)
        print(f"********\nOrder made! Total payment: ${total_cost}\n********")
    except ValueError as error:
        print(f"Error in processing order: {error}")
    except LookupError as error:  # Handling stock-related issues, if applicable
        print(f"Insufficient stock for one of the products: {error}")


def start(store: Store):
    """Starts the user interface to interact with the store."""
    while True:
        print("""
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")
        choice = input("Please choose a number: ")

        if choice == '1':
            list_all_products(store)
        elif choice == '2':
            show_total_amount(store)
        elif choice == '3':
            make_order(store)
        elif choice == '4':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Main function to start the store interaction
def main():
    """Main function to initialize the store and start the user interface."""
    start(best_buy)


if __name__ == "__main__":
    main()
