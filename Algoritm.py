import heapq
from typing import List, Tuple, Dict

class Graph:
    def __init__(self): 
        self.edges: Dict[str, List[Tuple[str, float]]] = {}

    def add_edge(self, from_node: str, to_node: str, distance: float):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, distance))

    def neighbors(self, node: str) -> List[Tuple[str, float]]:
        return self.edges.get(node, [])

class DijkstraOptimizer:
    def __init__(self, graph: Graph):
        self.graph = graph

    def find_shortest_path(self, start: str, end: str) -> Tuple[List[str], float]:
        queue = [] 
        heapq.heappush(queue, (0, start))
        distances = {start: 0} 
        previous_nodes = {start: None}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == end:
                break

            for neighbor, weight in self.graph.neighbors(current_node):
                distance = current_distance + weight
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

        path = []
        node = end
        while node is not None:
            path.append(node)
            node = previous_nodes[node]
        path.reverse()

        return path, distances.get(end, float('inf'))

def create_bacau_graph() -> Graph:
    graph = Graph()

    graph.add_edge("Centru", "Autogara", 0.99)
    graph.add_edge("Centru", "Cartier Nord", 1.89)
    graph.add_edge("Centru", "Cartier Sud", 1.56)
    graph.add_edge("Mall", "Autogara", 1.07)
    graph.add_edge("Mall", "Cartier Nord", 1.32)
    graph.add_edge("Autogara", "Cartier Sud", 2.41)

    return graph

def main():
    bacau_graph = create_bacau_graph()

    optimizer = DijkstraOptimizer(bacau_graph)
    start_location = "Mall"
    end_location = "Cartier Sud"

    shortest_path, total_distance = optimizer.find_shortest_path(start_location, end_location)

    print(f"Ruta optimă de la {start_location} la {end_location}: {shortest_path}")
    print(f"Distanța totală: {total_distance:.2f} km")

if __name__ == "__main__":
    main()

