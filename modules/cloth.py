class Clothing:
    """Composition"""
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        self.name = name

    def add_item(self, material, amount):
        self.stock['name'].append(self.name)
        self.stock['material'].append(material)
        self.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in self.stock['material']:
            if item == material:
                count += self.stock['amount'][n]
                n += 1
        return count

    def take_name(self):
        return self.name
