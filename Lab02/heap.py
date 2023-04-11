
import math

class Node:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority

    def __gt__(self,other):
        return self.priority > other.priority
    def __lt__(self,other):
        return self.priority < other.priority
    def __eq__(self, other):
        return self.priority == other.priority
    def __str__(self):
        return self.data

class min_heap:


    def __init__(self):
        self.heap = []


    def parent(self,i):
        if self.is_empty() ==0:
            return (i-1)//2
        return None


    def left_child(self,i):
        index = int(2*i+1)
        if index < len(self.heap):
            return index
        else:
            return -1

    def right_child(self,i):
        index = int(2*i+2)
        if index < len(self.heap):
            return index
        else:
            return -1
    def height(self):
        N = len(self.heap)
        h = math.log(N+1,2)
        return h
    def swap(self,a,b):
        self.heap[a],self.heap[b] = self.heap[b],self.heap[a]
    def is_empty(self):
        if len(self.heap) == 0:
            return 1
        return 0
      
    def reheap_up(self, index):
        if index == 0:
            return
        parent = self.parent(index)
        if self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.reheap_up(parent)

    def reheap_down(self):
        if self.is_empty() ==0 :
            
            index = 0
            highest_index = len(self.heap)-1
            while True:
                left_child_index = self.left_child(index)
                right_child_index = self.right_child(index)
                if left_child_index != -1: #there is at least one child
                    if left_child_index == highest_index: #this is the only child 
                        smaller_child_index = left_child_index
                    else: #there is a right child
                        if self.heap[right_child_index] < self.heap[left_child_index]: # checking the smaller child
                            smaller_child_index = right_child_index
                        else:
                            smaller_child_index = left_child_index
                
                    if self.heap[index] > self.heap[smaller_child_index]:
                        self.swap(index,smaller_child_index)
                        index = smaller_child_index
                    else:
                        break
            
                else:
                    break
            return
        else:
            return    
    def enqueue(self,node): #this is the node which has data and f
        self.heap.append(node)
        self.reheap_up(len(self.heap)-1)
    
    def dequeue(self):
        self.swap(0,len(self.heap)-1)
        hehe = self.heap.pop()
        self.reheap_down()
        return hehe.data

    def display(self):
        for i in self.heap:
            print(i)

class  Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self,x,y,g): #using every edge to update adjacency list
        arr = [y,g]
        if x in self.adj_list.keys():
            self.adj_list[x].append(arr)
        else:
            self.adj_list[x] = [arr]

    def display_adj_list(self):
        print(self.adj_list)  




if __name__ == '__main__':
    
    #graph
    graph = Graph()
    graph.add_edge('S','A',2)
    graph.add_edge('S','B',4)
    graph.add_edge('A','B',1)
    graph.add_edge('A','C',4)
    graph.add_edge('B','C',2)
    graph.add_edge('B','G',6)
    graph.add_edge('C','G',3)
    #graph.display_adj_list()


    h1 = {'S':8,'A':3,'B':7,'C':2,'G':0}
    h2 = {'S':7,'A':4,'B':5,'C':2,'G':0}
 
    
    





    



















