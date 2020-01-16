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

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            
            return None
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:

            return None
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next
    
    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = next
            _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):

        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        
        return new_head
    
    def remove_duplicates(self):

        cur = self.head
        prev = None

        dup_values = []

        while cur:
            if cur.data in dup_values:
                # Remove node
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before.
                dup_values.append(cur.data)
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n):

        p = self.head
        q = self.head

        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            return None
        
        while p and q:
            p = p.next
            q = q.next
        return p.data
    
    def count_occurences_iterative(self, data):

        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next

        return count

    def count_occurences_resursive(self, node, data):
        if not node:
            return 0
        
        if node.data == data:
            return 1 + self.count_occurences_resursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        p = self.head
        q = self.head

        prev = None
        count = 0

        while p and count < k:
            prev = p.next
            p = p.next
            q = q.next
            count += 1
        p = prev
        
        while q:
            prev = q
            q = q.next
        q = prev
        q.next = self.head
        self.head = p.next
        p.next = None

    def is_palindrome(self):
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def move_tail_to_head(self):
        prev = None
        cur = self.head
        while cur.next:
            prev = cur
            cur = cur.next
        prev.next = None
        cur.next = self.head
        self.head = cur

    def sum_to_list(self, llist):
        p = self.head
        q = llist.head
        result = []
        while p and q:
            if p:
                p_num = p.data
                p = p.next
            else:
                p_num = 0
            if q:
                q_num = q.data
                q = q.next
            else:
                q_num = 0
            result.append(p_num + q_num)

        return result
