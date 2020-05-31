def BFS(i):
    q = Queue(maxsize = len(a))
    visited = [0]*len(a)
    print(i)
    visited[i]=1
    q.put(i)
    while(len(q.queue)!=0):
        u = q.get(i)
        for v in range(len(a)):
            if a[u][v]==1 and visited[v]==0:
                print(v)
                visited[v]=1
                q.put(v) 