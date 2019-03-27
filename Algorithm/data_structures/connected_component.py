class Graph():
    def __init__(self, mydict = None):
        if mydict == None:
            self.gdict = {}
        else:
            self.gdict = mydict

    def addEdge(self, u, v, bidir = True):
        if u in self.gdict:
            self.gdict[u].append(v)
        else:
            self.gdict[u] = [v]
        
        if bidir:
            if v in self.gdict:
                self.gdict[v].append(u)
            else:
                self.gdict[v] = [u]

    def display_graph(self):
        print(self.gdict)

    def connected_component(self):
        visited = dict()
        for i in self.gdict:
            visited[i] = False
        comp_count = 0
        size_of_comp = []
        for i in self.gdict:
            if visited[i] == False:
                size_of_comp.append(0)
                self.dfs(visited, i, size_of_comp)
                comp_count += 1
                #print()
        return comp_count,size_of_comp

    def dfs(self, visited, source, size_of_comp):
        visited[source] = True
        size_of_comp[-1] += 1
        #print(source, end = ' ')
        for i in self.gdict[source]:
            if visited[i] == False:
                self.dfs(visited, i, size_of_comp)
