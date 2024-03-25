def Astar(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()
    g = {}
    par = {}
    g[start_node] = 0
    par[start_node] = start_node
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    par[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        par[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Đường đi không tồn tại!')
            return None

        if n == stop_node:
            path = []
            while par[n] != n:
                path.append(n)
                n = par[n]
            path.append(start_node)
            path.reverse()
            print('Tìm thấy đường đi : {}'.format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)
    print('Đường đi không tồn tại!')
    return None
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'S': 6,
        'A': 3,
        'B': 4,
        'C': 2,
        'D': 2,
        'G': 0,
    }
    return H_dist[n]

Graph_nodes = {
    'S': [('A', 3), ('B', 1)],
    'A': [('S', 3), ('B', 2), ('C', 1), ('G', 4), ('D', 3)],
    'B': [('S', 1), ('A', 2), ('C', 4)],
    'C': [('B', 4), ('A', 1), ('G', 3)],
    'D': [('A', 3), ('G', 2)],
    'G': [('D', 2), ('A', 4), ('C', 3)],
}

Astar('S', 'G')