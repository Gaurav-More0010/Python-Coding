#Basic
class Node:
    def __init__(self,value):
        self.value = value
        self.ref = None

# new_node = Node(10)
# print(new_node)

#_____________________________________________

# class LinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

# new_linked_list = LinkedList(10)
# print(new_linked_list)
# print(new_linked_list.head.value)
# print(new_linked_list.length)
#_______________________________________________

class LinkedList:
    def __init__(self):
        #new_node = Node()
        self.head = None
        self.tail = None
        self.length = 0
new_linked_list = LinkedList() 
print(new_linked_list.head.value)
print(new_linked_list.length)