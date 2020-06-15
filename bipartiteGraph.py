
def bipartiteBFS(g,v,color,src):
  
    queue = []
    queue.append(src)
    color[src]=1
    while len(queue)>0:
        u = queue.pop()
        for i in range(v):
            if g[u][v]==1 and color[v]==-1:
                color[v]=1-color[u]
                queue.append(v)
            elif g[u][v]==1 and color[v]==color[u]:
                return False
    
    
    return True

def bipartiteDFS(g,color,src,c):
    if color[src]!=-1 and color[src]!=c:
        return False
    color[src]=c
    ans = True
    for i in range(len(g)):
        if g[src][i]==1:
            if color[i]==-1:
                ans&=bipartiteDFS(g, color, i, 1-c)
            elif color[i]!=-1 and color[i]!=1-c:
                return False
    if ans==True:
        return True
    else:
        return False





v,e = list(map(int,input().split()))
g = [[0 for i in range(v)]for j in range(v)]
color= [-1 for i in range(v)]
for i in range(e):
    f,s = map(int,input().split())
    g[f-1][s-1] = 1
    g[s-1][f-1] = 1


res1 = bipartiteDFS(g,color,0,1)
res2 = bipartiteBFS(g,v,color,0)


"""
Complexity of the codes 
Matrix Representation = O(V^2)
Same for both BFS and DFS 
"""