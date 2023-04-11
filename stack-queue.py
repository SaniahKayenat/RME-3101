class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class Stack:
    def __init__(self):
        self.head = None
    def empty(self):
        if self.head == None: 
            return 1
        else: 
            return 0
        
    def push(self,value):
        new_node = Node(value)
        if self.empty() ==1:
            self.head = new_node
        else:
            n = self.head 
            while n.ref != None: 
                n = n.ref 
            n.ref = new_node
    def pop(self):
        n = self.head
        while n is not None:
            temp = n
            n = n.ref
        temp.ref = None
    def display(self):
        if self.empty() == 1:
            print ("Stack is empty!")
            return
        else:
            while self.head != None:
                print(f'{self.head.data}')
                self.head = self.head.ref
new_stack = Stack()
new_stack.push(12)
new_stack.push(15)
new_stack.push(1)
new_stack.push(45)
new_stack.push(44)
new_stack.pop()
new_stack.display()