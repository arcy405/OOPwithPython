import csv

class Item:
    pay_rate = 0.8
    all_items = []

    def __init__(self, name: str, price: float, quantity=0):
        # ... (unchanged)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path='items.csv'):
        try:
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f)
                items_list = list(reader)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return

        for item in items_list:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __str__(self):
        return f"{self.name}, {self.price}, {self.quantity}"

# Instances and usage
Item.instantiate_from_csv()
for item in Item.all_items:
    print(item)
  
