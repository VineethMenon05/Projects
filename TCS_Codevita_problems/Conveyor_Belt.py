from collections import defaultdict

def solve_conveyor_belt():
    N = int(input())
    child_to_parent = {}

    for _ in range(N):
        parts = input().split()
        junction = parts[0]
        for child in parts[1:]:
            child_to_parent[child] = junction

    workstations = input().split()
    K = int(input())

    switch_count = defaultdict(int)
    current_path = {}  # junction -> last outgoing path used

    total_time = 0

    for ws in workstations:
        path = []
        node = ws
        while node != "center":
            parent = child_to_parent[node]
            path.append((parent, node))
            node = parent

        for junction, next_node in path:
            total_time += 1

            if junction not in current_path or current_path[junction] != next_node:
                if switch_count[junction] < K:
                    total_time += 2
                    switch_count[junction] += 1
                    current_path[junction] = next_node
                else:
                    total_time += 3

    print(total_time, end='')

if __name__ == "__main__":
    solve_conveyor_belt()