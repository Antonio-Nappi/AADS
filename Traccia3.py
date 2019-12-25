from graph import Graph

def DFS(g,u):
'''Perform a depth-first search in a given graph g, starting from a given vertex u'''
    nodes = []                                  #nodes is the array of all discovered vertex
    nodes.append(u)
    for e in g.incident_edges(u, True):         
        if(e.opposite(u)._pre==None):
            tmp = e.opposite(u)                 #save in tmp the outgoing element not yet visited
            tmp._pre = u                        #save in the attribute ._pre of the element the precedent element
            nodes.append(tmp)
            i=0                                 #index that will be used to check if a vertex has still not visited vertex
            while(i < len(list(g.incident_edges(tmp)))):    
                if(list(g.incident_edges(tmp))[i].opposite(tmp)._pre == None and list(g.incident_edges(tmp))[i].opposite(tmp)!=u):
                    list(g.incident_edges(tmp))[i].opposite(tmp)._pre = tmp 
                    tmp = list(g.incident_edges(tmp))[i].opposite(tmp)  #if a not visited vertex is found, tmp is replaced by the new vertex untill there is not a deeper node 
                    nodes.append(tmp)
                    i=0
                else:
                    i=i+1                       #if there is anymore an edge that points to an univisted vertex change tmp with the precedent
                    if(i == len(list(g.incident_edges(tmp))) and tmp._pre!=u):
                        tmp= tmp._pre
                        i=0
    return nodes
