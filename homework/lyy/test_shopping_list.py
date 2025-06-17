import unittest
from shopping_list import ShoppingList

class TestShoppingList(unittest.TestCase):
    
    def setUp(self):
        self.shopping_list = ShoppingList({"帽子": 20,"内裤": 16,"短袖": 40})
        
    def test_get_shopping_list_number(self):
        self.assertEqual(self.shopping_list.get_shoppinglist_number(),3)
        
    def test_shopping_list_price(self):
        self.assertEqual(self.shopping_list.get_shoppinglist_price(),76)