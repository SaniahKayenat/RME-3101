#NEXT MEANS THE ADDRESS OF THE NEXT NODE
#self.head contains location of the node, self.head.next is the location that the node contains.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def empty(self):
        if self.head == None: #linked list is empty if there is no address at head
            return 1
        else: 
            return 0
    def traverse(self):
        if self.empty() == 1:
            print ("Linked List is empty!")
            return
        else:
            while self.head != None:
                print(self.head.data)
                self.head = self.head.next
    def add_begin(self,value):
        
            #----------adding at the beginning----------------
            #create new node
            #new_node.mext ==== previous head because its the first element now
            #head changed to new node object NEW NODE OBJECT IS BASICALLY THE LOCATION OF THE NEW NODE.
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
           
    def add_end(self,value):
        #----------addding at the end------------
        #traverse to the end node
        #change its next from null to new_node(location)
        new_node = Node(value)
        #if empty
        if self.empty() ==1:
            self.head = new_node
        else:
            n = self.head #address of first node #ASSIGN n TO THE LOCATION WE WANNA GO
            while n.next != None: #traversing till the last node because the last node contains null
                n = n.next #n.next is the "next" part of the node of the location assigned to n.
            n.next = new_node
    def add_after(self,value,x):
        n= self.head
        in_the_list = 0
        while n is not None:
            if n.data == x:
                in_the_list =1
                break
            n = n.next
        if in_the_list == 0:
            print (f'{x} not in the linked list')
            return
        else:
            new_node = Node(value)
            new_node.next = n.next
            n.next = new_node
    def add_before(self,value,x):
        n = self.head
        in_the_list = 0
        if self.empty() == 1:
            print (f"can't add before {x} since the linked list is empty")
            return 
        while n is not None:
            if n.data == x:
                in_the_list =1
                break
            temp=n
            n = n.next
        if in_the_list == 0:
            print (f'{x} not in the linked list')
            return
        else:
            
            new_node = Node(value)
            new_node.next = n
            temp.next = new_node
    def deletion(self,value):
        if self.empty():
            print(f'Linked list is empty')
        n = self.head
        in_the_list = 0
        while n is not None:
            if n.data == value:
                in_the_list =1
                break
            temp = n
            n =n.next
        if in_the_list:
            temp.next = n.next
        else:
            print(f'{value} not in the linked list')
    def clear(self):
        self.head = None
        return 
                     
LL1 = LinkedList()

#LL1.add_begin(12)
#LL1.add_end(30)
#LL1.add_begin(20)
#LL1.add_after(45,12)
#LL1.add_before(15,12)
#LL1.deletion(45)
#LL1.clear()
#LL1.traverse()