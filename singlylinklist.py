class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None

    def insert_at_head(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
                     
    def insert_at_tail(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node 

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp= temp.next
        print("None")      
    def search(self, key):
        n= self.head
        while n:
            if  n.data== key:
                return True
            n = n.next
        return False    
    def update(self,key,data):
        n=self.head
        while n :
            if n.data==key:
                n.data==data
                return
            n=n.next
        print("key {key} is not found")         
    def insert_after(self, key, data):
        new_node = Node(data)
        n = self.head
        while n:
            if n.data == key:
                new_node.next = n.next
                n.next = new_node
                return
            n= n.next
        print(f"Key {key} not found.")
    def insert_before(self, key, data):
        if  self.head is None:
            print("List is empty.")
            return
        if self.head.data== key:
            self.insert_at_head(data)
            return
        new_node = Node(data)
        n = self.head
        while n.next:
            if n.next.data == key:
                new_node.next = n.next
                n.next = new_node
                return
            n = n.next
        print(f"Key {key} not found.")
    def remove_from_head(self):
        if self.head is None:
            print('list is empty')
            return
        else:
            self.head=self.head.next
    def remove_from_tail(self):
        if self.head is None:
            print('list is empty')
            return
        else:
            n=self.head
            while n.next.next is not None:
                n=n.next
            n.next=None
    def remove_after(self, key):
        n = self.head
        while n and n.data != key:
                n = n.next
        if n and n.next:
           n.next = n.next.next

    def remove_before(self, key):
        if self.head.data == key or not self.head.next:
            return
        if self.head.next.data == key:
            self.head = self.head.next
            return
        
        prev = None
        n = self.head
        while n.next and n.next.data != key:
            prev = n
            n = n.next
        if prev:
            prev.next = n.next
obj = LinkList()
obj.insert_at_head(2)
obj.insert_at_head(3)
obj.insert_at_tail(9)
obj.insert_after(9,8)
obj.insert_before(2,6)
obj.display()
