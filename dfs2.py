# Python program to print DFS traversal from a 
# given given graph 
from collections import defaultdict 
  
# This class represents a directed graph using 
# adjacency list representation

data = defaultdict()
data[0] = [1,'Dinesh',2]
data[1] = [2,'Ramesh',4]
data[2] = [3,'Sandeep',4]
data[3] = [4,'Abhishek',4]
data[4] = [5,'Ravi',1]

class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A function used by DFS 
    def DFSUtil(self,v,visited): 
  
        # Mark the current node as visited and print it 
        visited[v]= True
        print ("<node name=%s id=%d>"%(data[v][1],data[v][0]))
        
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
        print("</node>")
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self,v): 
  
        # Mark all the vertices as not visited 
        visited = [False]*(len(self.graph)+1) 
        print(len(visited))
  
        # Call the recursive helper function to print 
        # DFS traversal 
        self.DFSUtil(v,visited) 
  
  
# Driver code 
# Create a graph given in the above diagram 
g = Graph() 
g.addEdge(3,1) 
g.addEdge(1,0)
g.addEdge(0,4)
g.addEdge(3,2) 
g.addEdge(0,0) 
g.addEdge(2,2)


  
print ("Following is DFS from (starting from vertex 4)")
g.DFS(3) 
  
# This code is contributed by Neelam Yadav 
