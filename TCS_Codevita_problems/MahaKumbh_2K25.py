from collections import defaultdict, deque
import sys

def find_path(graph, start, end, blocked_stations):
    if start == end:
        return True
    if start not in graph or end not in graph:
        return False
    visited = set([start])
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor in visited or neighbor in blocked_stations:
                continue
            if neighbor == end:
                return True
            visited.add(neighbor)
            queue.append(neighbor)
    return False

def main():
    lines = [line.rstrip('\n') for line in sys.stdin if line.strip() != '']
    idx = 0

    n = int(lines[idx].strip())
    idx += 1
    graph = defaultdict(set)

    for _ in range(n):
        parts = lines[idx].strip().split()
        idx += 1
        source = parts[0]
        stations = parts[1:]
        for station in stations:
            graph[source].add(station)
            graph[station].add(source)
        for i in range(len(stations)-1):
            graph[stations[i]].add(stations[i+1])
            graph[stations[i+1]].add(stations[i])

    q = int(lines[idx].strip())
    idx += 1
    queries = []
    for _ in range(q):
        if idx >= len(lines):
            break
        queries.append(lines[idx].strip())
        idx += 1

    r = 0
    restrictions = defaultdict(set)
    if idx < len(lines):
        r = int(lines[idx].strip())
        idx += 1
        for _ in range(r):
            if idx >= len(lines):
                break
            parts = lines[idx].strip().split()
            idx += 1
            src = parts[0].strip()
            blocked = [x.strip() for x in parts[1:]]
            restrictions[src].update(blocked)

    for i, query in enumerate(queries):
        query = query.strip()
        if " to " in query:
            parts = query.split(" to ")
            if len(parts) != 2:
                print("no", end='')
                if i < len(queries) - 1:
                    print()
                continue
            start, end = parts[0].strip(), parts[1].strip()
            blocked = restrictions.get(start, set())
            result = "yes" if find_path(graph, start, end, blocked) else "no"
            print(result, end='')
            if i < len(queries) - 1:
                print()
        elif " connects " in query:
            parts = query.split(" connects ")
            if len(parts) != 2:
                continue
            s1, s2 = parts[0].strip(), parts[1].strip()
            graph[s1].add(s2)
            graph[s2].add(s1)
        elif " disconnects " in query:
            parts = query.split(" disconnects ")
            if len(parts) != 2:
                continue
            s1, s2 = parts[0].strip(), parts[1].strip()
            graph[s1].discard(s2)
            graph[s2].discard(s1)

if __name__ == "__main__":
    main()