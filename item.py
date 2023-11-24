from inventory import Inventory

class Item(Inventory):
    def __init__(self,item_id,item_name,transaction_date):
        super().__init__(item_id,item_name)
        self._transaction_date = transaction_date

    def item_restock(self,quantity):
        self._available_stock += quantity
        print(f'Item restocked: {self.quantity} units on {self._transaction_date}')  

    def item_sale(self,quantity):
        if quantity <= self._available_stock:
            self._available_stock -= quantity
            print(f'{quantity} items sold and {self._available_stock} items remaining in stock')
        else:
            print(f'{quantity} items requested however they are more than the available stock of {self._available_stock}')

    def get_item_details(self):
        details =  super().get_item_details()
        print(f'{details}\n Transaction date: {self._transaction_date}')


        



