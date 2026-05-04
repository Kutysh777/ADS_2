from collections import deque
import heapq


graph = {
    'A': ['C', 'B', 'D'],
    'B': ['A', 'C', 'E', 'G'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'A'],
    'E': ['G', 'F', 'B'],
    'F': ['G', 'E'],
    'G': ['F', 'B'],
}


# TASK 1

def dfs(graph, source):

    marked = {}
    visit_order = []

    def _dfs(v, depth=0):
        indent = "  " * depth
        marked[v] = True
        visit_order.append(v)
        print(f"{indent}dfs({v})  →  marked: {v},  visit order so far: {visit_order}")

        for w in graph[v]:
            if w not in marked:
                print(f"{indent}  edge {v}-{w}: {w} not marked → recurse")
                _dfs(w, depth + 1)
            else:
                print(f"{indent}  edge {v}-{w}: {w} already marked → skip")

        print(f"{indent}return from dfs({v})")

    print("=" * 60)
    print(f"TASK 1 — DFS from source node: {source}")
    print("=" * 60)
    _dfs(source)
    print(f"\nDFS Visit Order: {' → '.join(visit_order)}\n")
    return visit_order



# TASK 2

def bfs(graph, source):

    print("=" * 60)
    print(f"TASK 2 — BFS from source node: {source}")
    print("=" * 60)

    marked = {}
    visit_order = []
    queue = deque()

    marked[source] = True
    queue.append(source)
    print(f"Enqueue {source}. Queue: {list(queue)}")

    step = 1
    while queue:
        v = queue.popleft()
        visit_order.append(v)
        print(f"\nStep {step}: Dequeue {v}  →  visit order so far: {visit_order}")
        step += 1

        for w in graph[v]:
            if w not in marked:
                marked[w] = True
                queue.append(w)
                print(f"  edge {v}-{w}: {w} not marked → enqueue {w}. Queue: {list(queue)}")
            else:
                print(f"  edge {v}-{w}: {w} already marked → skip")

    print(f"\nBFS Visit Order: {' → '.join(visit_order)}\n")
    return visit_order



# TASK 3

def task3_compare(dfs_result, bfs_result):
    print("=" * 60)
    print("TASK 3 — Implementation Comparison")
    print("=" * 60)
    print(f"DFS result (Task 1): {' → '.join(dfs_result)}")
    print(f"BFS result (Task 2): {' → '.join(bfs_result)}")

    dfs_match = dfs_result == ['A', 'C', 'B', 'E', 'G', 'F', 'D']
    bfs_match = bfs_result == ['A', 'C', 'B', 'D', 'E', 'G', 'F']

    print(f"\nExpected DFS: A → C → B → E → G → F → D")
    print(f"DFS matches expected: {'✓ YES' if dfs_match else '✗ NO'}")
    print(f"\nExpected BFS: A → C → B → D → E → G → F")
    print(f"BFS matches expected: {'✓ YES' if bfs_match else '✗ NO'}\n")


# TASK 4

def dijkstra(graph_weighted, source, target):

    dist = {v: float('inf') for v in graph_weighted}
    dist[source] = 0


    prev = {v: None for v in graph_weighted}


    heap = [(0, source)]

    visited = set()

    print("=" * 60)
    print(f"TASK 4 — Dijkstra's Shortest Path: {source} → {target}")
    print("=" * 60)
    print(f"\nInitial distances: { {v: (d if d != float('inf') else '∞') for v, d in dist.items()} }")

    step = 1
    while heap:
        current_dist, u = heapq.heappop(heap)

        if u in visited:
            continue
        visited.add(u)

        print(f"\nStep {step}: Process '{u}' (dist = {current_dist})")
        step += 1

        if u == target:
            break

        for neighbor, weight in graph_weighted[u]:
            if neighbor in visited:
                continue
            new_dist = current_dist + weight
            print(f"  Check edge {u}→{neighbor} (weight={weight}): "
                  f"new_dist={new_dist} vs current best={dist[neighbor] if dist[neighbor] != float('inf') else '∞'}", end="")
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = u
                heapq.heappush(heap, (new_dist, neighbor))
                print(f"  → Updated! dist[{neighbor}] = {new_dist}")
            else:
                print(f"  → No improvement.")


    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()

    print(f"\nShortest distance from {source} to {target}: {dist[target]} miles")
    print(f"Shortest path: {' → '.join(path)}\n")
    return dist[target], path


# Run


if __name__ == "__main__":

    # TASK 1
    dfs_order = dfs(graph, 'A')

    # TASK 2
    bfs_order = bfs(graph, 'A')

    # TASK 3
    task3_compare(dfs_order, bfs_order)

    # TASK 4
    scotland = {
        'Edinburgh': [('Stirling', 50), ('Dundee', 100), ('Glasgow', 70)],
        'Stirling':  [('Edinburgh', 50), ('Perth', 40), ('Glasgow', 50)],
        'Glasgow':   [('Stirling', 50), ('Edinburgh', 70)],
        'Perth':     [('Stirling', 40), ('Dundee', 60)],
        'Dundee':    [('Perth', 60), ('Edinburgh', 100)],
    }

    distance, path = dijkstra(scotland, 'Edinburgh', 'Dundee')

    print("=" * 60)
    print("SUMMARY — All Tasks")
    print("=" * 60)
    print(f"Task 1  DFS order : {' → '.join(dfs_order)}")
    print(f"Task 2  BFS order : {' → '.join(bfs_order)}")
    print(f"Task 4  Shortest  : {' → '.join(path)}  ({distance} miles)")
