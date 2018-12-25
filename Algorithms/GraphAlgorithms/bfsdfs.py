from collections import deque

def dfs(adj):
	def _dfs(v, adj, seen):
		seen[v] = True 
		# v's Preorder time
		for u in adj[v]:
			# u's Preorder time from v's perspective
			if not seen[u]: _dfs(u, adj, seen)
			# u's Postorder time from v's perspective
		print(v)
		#v's postorder time
	#Recall DFS in graphs requires a driver.
	N = len(adj)
	seen = [False]*N
	for i in range(N):
		if not seen[i]: _dfs(i, adj, seen)
	
def bfs(adj, v):
	seen = [False]*len(adj)
	Q = deque()
	Q.append(v)
	seen[v] = True 
	while len(Q) > 0:
		w = Q.popleft()
		print(w)
		for u in adj[w]:
			if not seen[u]:
				Q.append(u)
				seen[u] = True


adj = [[1, 2], [2], []]
dfs(adj)
bfs(adj, 0)
