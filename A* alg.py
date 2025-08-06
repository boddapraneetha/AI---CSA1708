from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}

def a_star(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    came_from = {}
    g_score = {start: 0}

    while not pq.empty():
        f, current = pq.get()

        if current == goal:
            # Reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for neighbor, cost in graph[current]:
            temp_g = g_score[current] + cost
            if neighbor not in g_score or temp_g < g_score[neighbor]:
                g_score[neighbor] = temp_g
                f_score = temp_g + heuristic[neighbor]
                pq.put((f_score, neighbor))
                came_from[neighbor] = current

    return None

path = a_star('A', 'F')
print("Shortest path from A to F:", path)
