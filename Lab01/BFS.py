#creating a class for graphs
class  Graph:
    def __init__(self,vertex_no,edge_no,starting_node):
        self.vertex_no = vertex_no
        self.edge_no = edge_no
        self.starting_node = starting_node
        self.adj_list = {}
        for i in range(vertex_no):
            self.adj_list[str(i)] = []
    
    def add_edge(self,x,y): #using every edge to update adjacency list
        self.adj_list[x].append(y)

    def display_adj_list(self):
        print(self.adj_list)    
        


#main code
if __name__ == '__main__':
    print("Please enter the numbers of vertices,the number of edges and the starting node\n")
    vertex_no = int(input())
    edge_no= int(input())
    starting_node = int(input())
    graph = Graph(vertex_no, edge_no, starting_node)

    while(edge_no): 
        print('Enter an edge:\n') 
        x,y = input(),input()
        graph.add_edge(x,y)
        edge_no-=1
    #graph.display_adj_list()

#BFS algorithm
    print("Enter test numbers\n")
    test = int(input())

    while(test):
        print("Enter your source and destination\n")
        s = input()
        d= input()
        from queue import Queue
        visited_vertices = {}
        level = {}
        parent = {}
        traversal_path = []
        queue = Queue() #creating an empty queue to generate the bfs traversal path
        #print(graph.adj_list)

        for vertex in graph.adj_list.keys():
            #INITIALLY
            visited_vertices[vertex] = False
            parent[vertex]= None
            level[vertex] = -1
        visited_vertices[s] = True #we will start by visiting the source
        level[s]= 0 #the level of the source is 0
        #parent[s] = None
        queue.put(s)

        while not queue.empty():
            u = queue.get() #pop the first elelement of the queue
            #print(u)
            traversal_path.append(u)
            for v in graph.adj_list[u]:
                if not visited_vertices[v]:
                    visited_vertices[v] = True
                    parent[v] = u
                    level[v] = level[u] +1
                    queue.put(v) #pushing the element to the queue

#is there a path from source to destination?
        path=[]
        
        while (d!=None):
            path.append(d)
            d = parent[d]
        path.reverse() # because we started from the destination and went to the source
        
        if path[0] == s:
            print(f'There is a path and that is {path}')
        else:
            print('There is no path')
        #print(traversal_path)
        #print(level)
        #print(parent)
        test-=1


    


















