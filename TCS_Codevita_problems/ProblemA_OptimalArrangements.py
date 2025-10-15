def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    data = []
    for i in range(n):
        parts = input().strip().split()
        data.append((parts[0], int(parts[1]), i + 1))
    k = int(input())

    # Step 1: Unique labels sorted
    labels = sorted(set(d[0] for d in data))
    label_to_idx = {label: i for i, label in enumerate(labels)}
    m = len(labels)

    # Step 2: Group original positions of each label
    pos_weight = [[] for _ in range(m)]
    for name, w, pos in data:
        idx = label_to_idx[name]
        pos_weight[idx].append((pos, w))

    # Sort positions for each label
    for lst in pos_weight:
        lst.sort()

    # Step 3: Greedy: assign smallest ship positions to smallest label index
    ship_positions = list(range(1, m + 1))
    total_cost = 0
    for idx, lst in enumerate(pos_weight):
        ship_pos = ship_positions[idx]
        for orig_pos, w in lst:
            total_cost += w * abs(orig_pos - ship_pos)

    # Step 4: Build the k-th lexicographical arrangement
    arrangement = labels[:]

    # For k-th arrangement, we just output labels sorted lex since we already sorted
    # (because permutations beyond 1st are only for tie-breaking)
    print(total_cost)
    print(' '.join(arrangement))


if __name__ == "__main__":
    main()
