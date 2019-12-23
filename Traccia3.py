def DFS(g,u):

    print(u)
    u._pre=u
    tmp=u
    for e in g.incident_edges(u):
        if(e._destination != u and e._destination._pre == None): #opposite al posto di destination
            tmp = e._destination
            tmp._pre = e._origin
            print(tmp._element)
            i=0
            while(i < len(list(g.incident_edges(tmp)))):
                if(list(g.incident_edges(tmp))[i]._destination != tmp and list(g.incident_edges(tmp))[i]._destination._pre == None):
                    list(g.incident_edges(tmp))[i]._destination._pre = tmp
                    print(list(g.incident_edges(tmp))[i]._destination._element)
                    tmp = list(g.incident_edges(tmp))[i]._destination
                    i=0
                else:
                    i=i+1
                    if(i == len(list(g.incident_edges(tmp))) and tmp._pre!=u):
                        tmp= tmp._pre
                        i=0
