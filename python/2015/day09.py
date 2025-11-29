example = [
    'London to Dublin = 464',
    'London to Belfast = 518',
    'Dublin to Belfast = 141',
]

def create_adjacency_matrix(lines: list[list[str]]) -> list[list[float]]:
    parts = [[line[0], line[2], int(line[4])] for line in lines]
    nodes = sorted(set(node for edge in parts for node in edge[:2]))
    n = len(nodes)
    matrix = [[float('inf')] * n for _ in range(n)]
    node_idx = { node: i for i, node in enumerate(nodes) }
    for start, end, distance in parts:
        i, j = node_idx[start], node_idx[end]
        matrix[i][j] = distance
        matrix[j][i] = distance

    # print(" "*9, " ".join(f"{node:>6}" for node in nodes))
    # for i, node in enumerate(nodes):
    #     print(f"{node:>7}: ", " ".join(f"{matrix[i][j]:>6}" if matrix[i][j] != float('inf') else "   inf" for j in range(n)))

    return matrix


class Graph():
    def __init__(self, n_edges):
        self.matrix = [[0 for _ in range(n_edges)] for _ in range(n_edges)]
        self.n_edges = n_edges

    def is_safe_to_add(self, node: int, pos: int, path: list[int]) -> bool:
        if self.matrix[path[pos-1]][node] == 0:
            return False

        for edge in path:
            if edge == node:
                return False

        return True

    def cycle_found(self, path: list[int], pos: int) -> bool:
        if pos == self.n_edges:
            if self.matrix[path[pos-1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(1, self.n_edges):
            if self.is_safe_to_add(v, pos, path):
                path[pos] = v

                if self.cycle_found(path, pos+1):
                    return True

                path[pos] = -1

        return False

    def find_hamiltonian_cycle(self) -> bool:
        path = [-1] * self.n_edges
        path[0] = 0
        if not self.cycle_found(path, 1):
            print('arse')
            return False

        print(path)
        return True


if __name__ == '__main__':
    matrix = create_adjacency_matrix([line.split(' ') for line in example])
    print(matrix)



# @dataclass
# class Node:
#     visited: bool = False
#     edges: list[tuple[str, int]] = field(default_factory=list)
#
#
# parts = [line.split(' ') for line in example]
# graph = defaultdict(Node)
# for line in parts:
#     graph[line[0]].edges.append((line[2], int(line[4])))
#     graph[line[2]].edges.append((line[0], int(line[4])))
#
# for k, v in graph.items():
#     print(f"{k:>7}: {v}")
