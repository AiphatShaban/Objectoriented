inventory = []
class Inventory:
    def __init__(self,item_id,item_name,available_stock):
        self._item_id = item_id
        self._item_name = item_name
        self._available_stock = available_stock

    def item_stock(self):
        return self._available_stock
    
    def item_id(self):
        return self._item_id
    
    def item_name(self):
        return self._item_name
    
    def get_item_details(self):
        print(f'Item_id: {self._item_id} \nItem_name: {self._item_name}\nAvailable Quantity: {self._available_stock}')

while True:
    print('Enter item details:')
    items = Inventory(int(input('Id:')),input('Name:'),int(input('Available stock: ')))
    inventory.append(items)
    more_items = input('Are there more items (Y/N)?:')
    if more_items.lower() == 'n':
        break
    else:
        continue

for items in inventory:
    Inventory.get_item_details(items)

            