class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

            return None
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_after_node(self, prev_node, data):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None

            return None
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return None
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        cur_pos = 0
        if cur_pos == pos:
            self.head = cur_node.next
            cur_node = None
            
            return None
        elif cur_pos > pos:

            return None
        prev = None
        while cur_node and cur_pos < pos:
            prev = cur_node
            cur_node = cur_node.next
            cur_pos += 1
        if cur_node is None:

            return None
        prev.next = cur_node.next
        cur_node = None
        

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.prepend("C")
prev_node = llist.head.next
llist.insert_after_node(prev_node, "E")
llist.print_list()
llist.delete_node("C")
llist.print_list()
llist.delete_node_at_pos(2)
llist.print_list()
