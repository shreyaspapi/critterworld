from collections import deque, defaultdict
input = open("1.txt", "r")
content = input.readlines()
t = int(content[0])
for i in range(t):
    n,m = map(int, content[i+1].split())
    
    # initializing BFS
    adj = defaultdict(list)
    dis = dict([])
    vis = dict()
   
    for k in range(1,n+1):
        dis[k] = 0
        vis[k] = False
       
    for j in  range(n-1):
        a,b = map(int, content[i+2].split())
        adj[a].append(b)
       
    que = deque([])
    que.append(1)
    vis[1] = True
    dis[1] = 0
    while que:
        u = que.popleft()
        for v in adj[u]:
            vis[v] = True
            dis[v] = 1+ dis[u]
            que.append(v)
    M = list(map(int, content[i+3].strip(" ").split()))
    s = 0
    for l in M:
        s += dis[l]
    ans = 2*(s)/m
   
    print("%0.6f"%ans)
