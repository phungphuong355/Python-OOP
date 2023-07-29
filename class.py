from modules.cloth import Clothing


class Shirt(Clothing):
    material = "Cotton"


class Saints(Clothing):
    material = "Cotton"


polo = Shirt("Polo")
sweatpants = Saints("Sweatpants")

polo.add_item(material=polo.material, amount=4)
sweatpants.add_item(material=sweatpants.material, amount=6)

current_stock1 = polo.Stock_by_Material(material="Cotton")
current_stock2 = sweatpants.Stock_by_Material(material="Cotton")

print(polo.stock)
print(sweatpants.stock)
print(current_stock1, current_stock2)
