from heapq import heappop, heappush
from itertools import count

def a_star(graph, start, goal, heuristic):
    tie_breaker = count()
    frontier = [(heuristic[start], next(tie_breaker), start)]
    came_from = {}
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0
    closed = set()

    while frontier:
        _, _, current = heappop(frontier)
        if current in closed:
            continue
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1], g_score[goal]
        closed.add(current)

        for neighbor, cost in graph.get(current, []):
            tentative_g = g_score[current] + cost
            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                heappush(
                    frontier,
                    (tentative_g + heuristic.get(neighbor, 0),
                     next(tie_breaker), neighbor),
                )
                closed.discard(neighbor)
    return None, float("inf")

if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("D", 2), ("E", 5)],
        "C": [("F", 1)],
        "D": [("G", 2)],
        "E": [("G", 1)],
        "F": [("G", 3)],
        "G": [],
    }
    heuristic = {"A": 7, "B": 6, "C": 2, "D": 1, "E": 0, "F": 3, "G": 0}
    path, cost = a_star(graph, "A", "G", heuristic)
    print("Shortest path using A*:", path)
    print("Path cost:", cost)
