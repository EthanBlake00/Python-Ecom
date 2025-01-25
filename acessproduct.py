from product import Product

contain = input("Create or Update product: ")
product1 = Product("", 0, 0)

if contain.lower() == "create":
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    qty = input("Enter product quantity: ")

    product1.name = name
    print(product1.get_details())

elif contain.lower() == "update":
    price = input("Enter product price: ")

    product1.update_price(1100000)
    print(product1.get_details())



