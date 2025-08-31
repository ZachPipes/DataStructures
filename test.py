from Structures.MyLinkedList import MyLinkedList, MyNode
from Structures.MyHashMap import MyHashMap
import unittest

def test():
    # Discover all tests in the 'tests' folder
    loader = unittest.TestLoader()
    suite = loader.discover("Tests")  # adjust folder name

    runner = unittest.TextTestRunner()
    runner.run(suite)

test()

# ll = MyLinkedList()
#
# for i in range(0, 3):
#     ll.insert_at_head(i)
# node = ll.find(1)
# print(ll)
# print(node.value)
#
# myMap = MyHashMap()
# myMap.put("a", 1)
# print(myMap.get("a"))

# myMap = MyHashMap()
# myMap.put("x", [42, 3, 5])
# myMap.put("ab", 2)
# result = str(myMap)
# print(result)