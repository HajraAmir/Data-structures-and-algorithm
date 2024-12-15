"""class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Doublylinklist:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        n = self.head
        while n.next:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def update(self, key, data):
        n = self.head
        while n:
            if n.data == key:
                n.data = data
                return
            n = n.next
        print(f"{key} node not found")

    def search(self, key):
        n = self.head
        while n:
            if n.data == key:
                return True
            n = n.next
        return False

    def display(self):
        n = self.head
        while n:
            print(n.data, end=" --> ")
            n = n.next
        print('None')

    def insert_after(self, key, data):
        new_node = Node(data)
        n = self.head
        while n:
            if n.data == key:
                new_node.next = n.next
                new_node.prev = n
                if n.next:
                    n.next.prev = new_node
                n.next = new_node
                return
            n = n.next
        print(f"{key} node not found")

    def insert_before(self, key, data):
        if self.head is None or self.head.data == key:
            self.insert_at_head(data)
            return
        new_node = Node(data)
        n = self.head
        while n.next:
            if n.next.data == key:
                new_node.next = n.next
                new_node.prev = n
                if n.prev:
                    n.prev.next = new_node
                n.next.prev = new_node
                n.next = new_node
                return
            n = n.next
        print(f"{key} node not found")

obj = Doublylinklist()
obj.insert_at_head(7)
obj.insert_at_tail(6)
obj.insert_at_head(9)
obj.insert_at_head(4)
obj.insert_after(9,2)
obj.insert_before(6,1)
obj.display()"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Doublylinklist:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        n = self.head
        while n.next:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def update(self, key, data):
        n = self.head
        while n:
            if n.data == key:
                n.data = data
                return
            n = n.next
        print(f"{key} node not found")

    def search(self, key):
        n = self.head
        while n:
            if n.data == key:
                return True
            n = n.next
        return False

    def display(self):
        n = self.head
        while n:
            print(n.data, end=" --> ")
            n = n.next
        print('None')

    def insert_after(self, key, data):
        new_node = Node(data)
        n = self.head
        while n:
            if n.data == key:
                new_node.next = n.next
                new_node.prev = n
                if n.next:
                    n.next.prev = new_node
                n.next = new_node
                return
            n = n.next
        print(f"{key} node not found")

    def insert_before(self, key, data):
        if self.head is None:
            print(f"List is empty.")
            return
        if self.head.data == key:
            self.insert_at_head(data)
            return
        new_node = Node(data)
        n = self.head
        while n.next:
            if n.next.data == key:
                new_node.next = n.next
                new_node.prev = n
                n.next.prev = new_node
                n.next = new_node
                return
            n=n.next
        print(f"{key} node not found")
    def remove_at_head(self):
        if self.head is None:
            print("List is empty. Nothing to remove.")
            return
        if self.head.next is None:
            self.head=None
            return
        self.head=self.head.next
        self.head.prev=None
        
    def remove_at_tail(self):
        if self.head is None:
            print('list is empty')
            return
        if self.head.next is None:
            self.head=None
            return
        n=self.head
        while n.next.next is not None:        
            n=n.next
        n.next=None     
    """def remove_after(self,key):
        if self.head is None:
            print('list is empty')
            return
        n=self.head
        while n and n.data !=key:
            n=n.next
        n.next=n.next.next   """ 
    def remove_before(self, key):
        if self.head is None or self.head.next is None:
            print("List is empty or contains only one node. Cannot remove before.")
            return
        if self.head.next.data == key:
            self.remove_at_head()
            return
        prev = None
        n= self.head
        while n.next:
            if n.next.data == key:
                if prev:
                    prev.next = n.next
                    n.next.prev = prev
                    return
                else:
                    print("No node found before the specified key.")
                    return
            prev = n
            n= n.next
        print(f"No node found with data {key}")

    def remove_after(self, key):
        if self.head is None:
            print("List is empty. Nothing to remove.")
            return
        n = self.head
        while n:
            if n.data == key and n.next:
                n.next = n.next.next
                if n.next:
                    n.next.prev = n
                return
            n = n.next
        print(f"No node found with data {key} or it is the last node.")     
        
        
        
        
        
        
        
        
obj = Doublylinklist()
obj.insert_at_head(7)
obj.insert_at_tail(6)
obj.insert_at_head(9)
  
obj.insert_at_head(4)
obj.insert_after(9,2)
obj.insert_before(6,1)
obj.remove_after(4)
obj.remove_before(6)

obj.display()
