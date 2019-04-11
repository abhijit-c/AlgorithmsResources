def floydwarshall(G):
    """
    Compute and return the all pairs shortest paths solution.
    Notice the returned path cost matrix P has modified entries. For
    example, P[i][j] contains a tuple (c, v1) where c is the cost of the
    shortest path from i to j, and v1 is the first vertex along said path
    after i. If there is no such vertex, then it is -1.
    """
    N = len(G)
    P = [[(G[i][j],j) for j in range(N)] for i in range(N)]
    for i in range(N):
        P[i][i] = (0, -1) 
    for k in range(N):
        for i in range(N):
            for j in range(N):
                alt = P[i][k][0] + P[k][j][0] 
                if P[i][j][0] > alt: 
                    P[i][j] = (alt, P[i][k][1]) 
    return P

def printpath(P, u, w):
    """
    Given modified path cost matrix (see floydwarshall) return shortest path
    from i to j.
    """
    path = [u]
    while P[u][w][1] != -1:
        path.append(P[u][w][1])
        u = P[u][w][1]
    return path

def pprint(matrix): #https://stackoverflow.com/questions/13214809/
    """
    Pretty print matrix with proper spacing. Don't worry about this.
    """
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

'''
Let us create the following weighted graph (graph art stolen from g4g)
            10 
       (0)------->(3) 
        |         /|\ 
      5 |          | 
        |          | 1 
       \|/         | 
       (1)------->(2) 
            3           
'''

inf = float('inf')
G = [   [inf , 5  , inf, 10 ],
        [inf , inf, 3  , inf],
        [inf , inf, inf, 1  ],
        [inf , inf, inf, inf]]

print('Edge Cost Matrix')
pprint(G)
P = floydwarshall(G)
print('Path Cost Matrix')
pprint(P)
print(printpath(P, 0, 2))
