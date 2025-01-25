from customer import Customer


class Order:
    def __init__(self, customer: Customer, order_id):
        self.customer = customer
        self.order_id = order_id
        self.products = []
        self.total = 0

    def add_product(self, product):
        self.products.append(product)

    def calculate_product(self):
        self.total = sum(product.price for product in self.products)

    def generate_summery(self):
        summary = (f"Order ID: ${self.order_id}\n"
                   f"Customer: {self.customer.name}\n"
                   f"Products:\n")
        for product in self.products:
            summary += f"-{product.get_details()}\n"
        summary += f"Total: Rs{self.total}"
