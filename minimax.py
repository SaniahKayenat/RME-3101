import math
class Node:
    def __init__(self,node_name, val):
        self.node_name = node_name
        self.val = val
    
class Tree:
    def __init__(self):
        self.adj_list = {}
    def add_edge(self,x,y):
        if x.node_name in self.adj_list.keys():
            self.adj_list[x.node_name].append(y) #appending the node, not just the name
        else:
            self.adj_list[x.node_name] = list()
            self.adj_list[x.node_name].append(y)
    
class Minimax:
    def __init__(self,tree):
        self.tree = tree
    def value(self,node,flag):
        if flag == 0:
            return node.val
        elif flag == 1:
            return self.max_val(node)
        elif flag == -1:
            return self.min_val(node)

    def max_val(self,node):
        v = -math.inf
        if node.val == None:
            successor_arr = self.tree.adj_list[node.node_name]
            for child in successor_arr:
                v = max(v,self.value(child,-1))
        else:
            return self.value(node,0)
        return v
    
    def min_val(self,node):
        v = math.inf
        if node.val == None:
            successor_arr = self.tree.adj_list[node.node_name]
            for child in successor_arr:
                v = min(v,self.value(child,1))
        else:
            return self.value(node,0)
        return v

n1 = Node('S',None)
n2 = Node('S',3)
n3 = Node('S',5)

tree = Tree()
tree.add_edge(n1,n2)
tree.add_edge(n1,n3)

minmax = Minimax(tree)
print(minmax.value(n1,1))