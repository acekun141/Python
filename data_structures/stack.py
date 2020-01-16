"""
Stack Data Structure.
"""

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        top = self.items.pop()
        return top

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


if __name__ == "__main__":
    s = Stack()
    s.push("A")
    s.push("B")
    print(s.get_stack())
    s.pop()
    print(s.get_stack())
