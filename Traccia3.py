from TdP_collections.graphs.graph import Graph

def DFS(g,u):
    print(u)
    u.visited=True
    node=1;
    j=0
    while (j < len(list(g.incident_edges(u)))):
        i=0
        tmp=list(g.incident_edges(u))[j]._destination
        while(i < len(list(g.incident_edges(tmp)))):
            if(list(g.incident_edges(tmp))[i]._destination.visited==False):
                list(g.incident_edges(tmp))[i]._destination.visited=True
                print(list(g.incident_edges(tmp))[i]._destination._element)
                tmp=list(g.incident_edges(tmp))[i].opposite(tmp)
                i=0
                node=node+1
            else:
                i=i+1
        i=0
        while(i < len(list(g.incident_edges(tmp)))):
            if(list(g.incident_edges(tmp))[i]._origin.visited==False):
                list(g.incident_edges(tmp))[i]._origin.visited=True
                print(list(g.incident_edges(tmp))[i]._origin._element)
                tmp=list(g.incident_edges(tmp))[i].opposite(tmp)
                i=0
                node=node+1
            else:
                i=i+1
        j=j+1
