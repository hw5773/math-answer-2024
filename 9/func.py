import logging

# load_graph: str * int -> set * dict
def load_graph(fname, is_undirected=False, allow_multiple=False, allow_loop=False):
    logging.info("Loading a graph from {}".format(fname))
    logging.debug("  is_undirected: {}".format(is_undirected))
    logging.debug("  allow_multiple: {}".format(allow_multiple))
    logging.debug("  allow_loop: {}".format(allow_loop))

    vertex = set([])
    edge = {}

    # make a set of vertices first
    with open(fname, "r") as f:
        for line in f:
            u, v = line.strip().split(",")
            vertex.add(u)
            vertex.add(v)

    for u in vertex:
        edge[u] = {}
        for v in vertex:
            edge[u][v] = 0

    # make a dictionary of edges
    with open(fname, "r") as f:
        for line in f:
            u, v = line.strip().split(",")
            edge[u][v] += 1

    if is_undirected:
        for u in vertex:
            for v in vertex:
                edge[u][v] += edge[v][u]
                edge[v][u] = edge[u][v]

        for u in vertex:
            for v in vertex:
                edge[u][v] = int(edge[u][v] / 2)

    if not allow_loop:
        for v in vertex:
            edge[v][v] = 0

    if not allow_multiple:
        for u in vertex:
            for v in vertex:
                if edge[u][v] > 0:
                    edge[u][v] = 1

    return vertex, edge
