from Structures.MyLinkedList import MyLinkedList, MyNode

ll = MyLinkedList()

for i in range(0, 3):
    ll.insert_at_head(i)
node = ll.find(1)
print(ll)
print(node.value)