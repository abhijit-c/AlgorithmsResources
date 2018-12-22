def floydwarshall(G):
	N = len(G)
	dist = [[(G[i][j],j) for j in range(N)] for i in range(N)]
	for i in range(N):
		dist[i][i] = (0, -1) 
	for k in range(N):
		for i in range(N):
			for j in range(N):
				alt = dist[i][k][0] + dist[k][j][0]
				if dist[i][j][0] > alt: 
					dist[i][j] = (alt, dist[i][k][1]) 
	return dist
