from collections import deque
from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.neighborgs = []


class Graph(Generic[T]):
    def __init__(self, root: Node[T] = None):
        self.root = root
        self.nodes = []

    def add_node(self, node: Node[T]):
        self.nodes.append(node)

    def print_graph(self, start_node: Node[T] = None):
        if start_node not in self.nodes:
            raise ValueError('Node not in graph')

        visited_nodes = []

        print(f'{start_node.data}')

        nodes_to_visit = deque()
        nodes_to_visit.append(start_node)
        while nodes_to_visit:
            parent_node = nodes_to_visit.popleft()

            for child_node in parent_node.neighborgs:
                if child_node not in visited_nodes and child_node not in nodes_to_visit:
                    nodes_to_visit.append(child_node)
                    print(f'{parent_node.data}->{child_node.data}', end=' | ')

            visited_nodes.append(parent_node)
            print('')


# Criando nós
nodes = {char: Node(char) for char in "ABCDEFGHIJKLMN"}

# Conectando os nós (criando arestas)
nodes['A'].neighborgs.extend([nodes['B'], nodes['C'], nodes['D']])
nodes['B'].neighborgs.extend([nodes['E'], nodes['F']])
nodes['C'].neighborgs.extend([nodes['G'], nodes['H']])
nodes['D'].neighborgs.extend([nodes['I']])
nodes['E'].neighborgs.extend([nodes['J']])
nodes['F'].neighborgs.extend([nodes['K'], nodes['L']])
nodes['G'].neighborgs.extend([nodes['M']])
nodes['H'].neighborgs.extend([nodes['N']])
nodes['I'].neighborgs.extend([nodes['L'], nodes['N']])

# Criando o grafo e adicionando os nós
graph = Graph(nodes['A'])
for node in nodes.values():
    graph.add_node(node)

# Testando print_graph a partir do nó A
graph.print_graph(nodes['A'])

