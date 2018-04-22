class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found is None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found is None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        edge_list = []
        for edge in self.edges:
            edge_graph = ()
            edge_graph = edge_graph + (edge.value, edge.node_from.value, edge.node_to.value)
            edge_list.append(edge_graph)
        pass
        return edge_list

    @property
    def get_adjacency_list(self):
        edges_list = []
        adjacency_list = []

        def check_exist_edge_by_val(edge_val):
            nonlocal edges_list
            if edge_val not in edges_list:
                return False
            return True

        for i in range(len(self.nodes) + 1):
            if i == 0:
                adjacency_list.append(None)
                continue
            neighboors = []
            for edge in self.nodes[i - 1].edges:
                neighboor = ()
                if not check_exist_edge_by_val(edge.value):
                    edges_list.append(edge.value)
                    neighboor = neighboor + (edge.node_to.value, edge.value)
                    neighboors.append(neighboor)
            if len(neighboors) is 0:
                adjacency_list.append(None)
            else:
                adjacency_list.append(neighboors)
        return adjacency_list

    def get_adjacency_matrix(self):
        matrix = [[0 for i in range(len(self.nodes) + 1)] for i in range(len(self.nodes) + 1)]
        edges_list = []

        def check_exist_edge_by_val(edge_val):
            nonlocal edges_list
            if edge_val not in edges_list:
                return False
            return True

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == 0 or j == 0 or i == j:
                    continue
                else:
                    for edge in self.nodes[i - 1].edges:
                        if edge.node_to.value == j:
                            if not check_exist_edge_by_val(edge.value):
                                edges_list.append(edge.value)
                                matrix[i][j] = edge.value
        return matrix


graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print(graph.get_edge_list())
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print(graph.get_adjacency_list)
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print(graph.get_adjacency_matrix())
