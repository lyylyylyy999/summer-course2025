class ShoppingList:
    def __init__(self,shopping_list):
        self.shopping_list = shopping_list
    
    def get_shoppinglist_number(self):
        return len(self.shopping_list)
    
    def get_shoppinglist_price(self):
        total_price = 0
        for price in self.shopping_list.values():
            total_price += price
        return total_price
        
# shopping_list = ShoppingList({"帽子": 20,"内裤": 16,"短袖":40})

# print(f"商品的数量为：{shopping_list.get_shoppinglist_number()}")
# print(f"商品的总价格为：{shopping_list.get_shoppinglist_price()}")