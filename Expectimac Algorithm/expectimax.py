import math 
class Node:
    def __init__(self,node_name,val,probability):
        self.node_name = node_name
        self.probability = probability
        self.val = val

class Tree:
    def __init__(self):
        self.adj_list = {}
    def add_edge(self,x,y):
        if x.node_name in self.adj_list.keys():
            self.adj_list[x.node_name].append(y)
        else:
            self.adj_list[x.node_name] = list()
            self.adj_list[x.node_name].append(y)

class expectimax:
    def __init__(self,tree):
        self.tree = tree
        self.chances = {}
    
    def max_value(self, node):
        v = -math.inf
        successor_arr = self.tree.adj_list[node.node_name]
        for child in successor_arr:
            if child.val != None:
                v = max(v,self.value(child,0))
                
            else:
                v = max(v,self.value(child,-1))
                
        return v

    def exp_value(self,node):
        v = 0
        successor_arr = self.tree.adj_list[node.node_name]
        for child in successor_arr:
            if child.val != None:
                p = child.probability
                v += p*child.val
            else:
                v = min(v,self.value(child,1))
        self.chances[node.node_name] = v
        return v
            


    def value(self,node,flag):
        if flag == 0: #terminal
            return node.val
        elif flag == 1: #max
            return self.max_value(node)
        elif flag == -1: #exp
            return self.exp_value(node)
    

n1= Node('A',None,None)
n2=Node('B',None,None)
n3=Node('C',None,None)
n4=Node('D',None,None)
n5=Node('E',3,0.1)
n6=Node('F',12,0.9)
n7=Node('G',50,0.01)
n8=Node('H',2,0.99)
n9=Node('I',4,0.1)
n10=Node('J',6,0.9)


tree = Tree()
tree.add_edge(n1,n2)
tree.add_edge(n1,n3)
tree.add_edge(n1,n4)
tree.add_edge(n2,n5)
tree.add_edge(n2,n6)
tree.add_edge(n3,n7)
tree.add_edge(n3,n8)
tree.add_edge(n4,n9)
tree.add_edge(n4,n10)


algo = expectimax(tree)
print(algo.value(n1,1))
chances_values = algo.chances.values()
max_chance = max(chances_values)
for key in algo.chances:
    if algo.chances[key] == max_chance:
        print(key)

#print(tree.adj_list)



