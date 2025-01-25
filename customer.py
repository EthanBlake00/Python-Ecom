class Customer:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact

    def __str__(self):
        return f"Name {self.name}, Address {self.address}, Contact ${self.contact}"
