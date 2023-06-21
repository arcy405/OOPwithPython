class Item:
    pay_rate = 0.8  # the oay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):

        # run validation to the received arguments
        assert price >= 0, f"price {price} is greater than or equal to zero"
        assert quantity >= 0, f"quantity {quantity} is greater than or equal to zero"

        # assign to self object
        # print(f"An instance created: {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("phone", 100 )
# item1.name = "phone"
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))


item2 = Item("laptop", 2000, 4)
item2.has_numpad = True
# item2.name = "laptop"
# item2.price = 2000
# item2.quantity = 2
# print(item2.calculate_total_price(item2.price, item2.quantity))


# print(type(item1))
# print(type(item1.name))

# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)
# print(item2.has_numpad)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price() )

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)
#
print(Item.__dict__)
print(item1.__dict__)
print(item2.__dict__)

item1.apply_discount()
print(item1.price)

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
