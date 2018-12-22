import heapq

def decrease_key(heap, v, val):
	"""
	In heap change key (_, v) to (val, v) and maintain heap.

	Below runs in O(len(heap)), but theoretically we can achieve this step in
	logarithmic time. However, to do so I have to open up the internals of the
	heapq structure, and we sacrifice a lot in the readability of the dijkstra,
	so we forgo it here. I swear I'm not being lazy... See this documentation
	page for an idea on how to do it:
	https://docs.python.org/3.7/library/heapq.html#priority-queue-implementation-notes
	"""
	for i in range(len(heap)):
		if heap[i][1] == v:
			heap[i] = (val, v)
			heapq._siftup(heap, i) #Accessing _ methods is bad practice
			break

def dijkstra(G, s):
	"""
	Find shortest paths on directed G with source s
	
	Note G is a modified adjacency list here, G[i] denotes the neighbors of
	vertex i, and in this list are entries of form (n, e_in) where n is said
	neighbor of i, and e_in is the cost of the edge i -> n.
	"""
	# Construct heap of format (priority_of_i, i) 
	pq = [(float('inf'), i) for i in range(0,len(G))]
	pq[s] = (0, s)
	# Maintain dist vector, where the vth entry is (cost_{s -> v}, parent_of_v)
	dist = [(c, None) for (c,_) in pq]
	# Turn pq into a heap
	pq[0], pq[s] = pq[s], pq[0]
	# Check to see if done, and if not done, if we've explored our whole
	# connected component. Order is important due to short circuit behavior.
	while pq != [] and pq[0][1] != float('inf'):
		(cost, v) = heapq.heappop(pq)
		for (u, e_vu) in G[v]: #Try to update new child of v
			alt = e_vu + cost
			if alt < dist[u][0]: 
				dist[u] = (alt, v)
				decrease_key(pq, u, alt) #Maintain heap invariant
	return dist

G = [[(1, 1), (2, 1)], [(2, 1)], []]
dist = dijkstra(G, 0)
print(dist)
