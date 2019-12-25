from graph import Graph
def DFS(g,u):
    nodes = []
    nodes.append(u)
    for e in g.incident_edges(u, True):
        if(e.opposite(u)._pre==None):
            tmp = e.opposite(u)
            tmp._pre = u
            nodes.append(tmp)
            i=0
            while(i < len(list(g.incident_edges(tmp)))):
                if(list(g.incident_edges(tmp))[i].opposite(tmp)._pre == None and list(g.incident_edges(tmp))[i].opposite(tmp)!=u):
                    list(g.incident_edges(tmp))[i].opposite(tmp)._pre = tmp
                    tmp = list(g.incident_edges(tmp))[i].opposite(tmp)
                    nodes.append(tmp)
                    i=0
                else:
                    i=i+1
                    if(i == len(list(g.incident_edges(tmp))) and tmp._pre!=u):
                        tmp= tmp._pre
                        i=0
    for v in nodes:
        print(v._element)
