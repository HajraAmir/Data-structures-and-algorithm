class Node:
    def __init__(self, data):
        self.data = data
       
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node  # Circular link to itself
            self.head = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node  # Circular link to itself
            self.head = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node

    def remove_at_head(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            self.head.next = self.head.next.next

    def remove_at_tail(self):
        if not self.head:
            print("List is empty.")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head.next
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head

    def insert_before(self, key, data):
        if not self.head:
            print("List is empty.")
            return
        if self.head.data == key:
            self.insert_at_head(data)
            return
        prev = None
        temp = self.head.next
        while temp != self.head:
            if temp.data == key:
                new_node = Node(data)
                new_node.next = temp
                prev.next = new_node
                return
            prev = temp
            temp = temp.next
        print(f"Key {key} not found.")

    def insert_after(self, key, data):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head.next
        while temp != self.head:
            if temp.data == key:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print(f"Key {key} not found.")

    def remove_before(self, key):
        if not self.head:
            print("List is empty.")
            return
        if self.head.data == key:
            print("Cannot remove node before head.")
            return
        prev = None
        temp = self.head.next
        while temp != self.head:
            if temp.data == key:
                if prev == self.head:
                    self.remove_at_tail()
                else:
                    prev.next = temp
                return
            prev = temp
            temp = temp.next
        print(f"Key {key} not found.")

    def remove_after(self, key):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head.next
        while temp != self.head:
            if temp.data == key:
                if temp.next == self.head:
                    print("Cannot remove node after the last node.")
                else:
                    temp.next = temp.next.next
                return
            temp = temp.next
        print(f"Key {key} not found.")
