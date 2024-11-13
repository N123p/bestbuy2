from products import Product, NonStockedProduct, LimitedProduct
from store import Store
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree

# Setup initial stock of inventory with promotions
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    NonStockedProduct("Windows License", price=125),
    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

# Create promotion instances
second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent_off = PercentDiscount("30% off", percent=30)

# Add promotions to selected products
product_list[0].set_promotion(second_half_price)  # MacBook Air M2
product_list[1].set_promotion(third_one_free)  # Bose QuietComfort Earbuds
product_list[3].set_promotion(thirty_percent_off)  # Windows License

# Create a store with the products
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
    """Handles creating an order by prompting user input for product and quantity."""
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


            if isinstance(product, LimitedProduct) and quantity > product.maximum:
                print(f"Error while making order! Only {product.maximum} is allowed from this product!")
                return

            shopping_list.append((product, quantity))
            print("Product added to list!")

        except ValueError:
            print("Invalid input. Please enter a valid product number and quantity.")
        except IndexError:
            print("Invalid product number. Please select a number from the list.")

    try:
        total_cost = store.order(shopping_list)
        print(f"********\nOrder made! Total payment: ${total_cost:.2f}\n********")
    except ValueError as error:
        print(f"Error in processing order: {error}")
    except LookupError as error:
        print(f"Insufficient stock for one of the products: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")


    return





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



def main():
    """Main function to initialize the store and start the user interface."""
    start(best_buy)


if __name__ == "__main__":
    main()
