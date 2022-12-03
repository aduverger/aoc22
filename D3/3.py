def get_priority(item: str) -> int:
    ordinal = ord(item)
    if ordinal > 96:
        return ordinal - 96
    return ordinal - 38


groups = []
group_count = 3
p1_sum_priorities = 0
p2_sum_priorities = 0

for line in open("3.txt"):
    line = line.strip()
    # PART 1
    mid = len(line) // 2
    first_compartment = line[:mid]
    second_compartment = line[mid:]
    for item in second_compartment:
        if item in first_compartment:
            p1_sum_priorities += get_priority(item)
            break
    # PART 2
    if group_count >= 3:
        groups.append([line])
        group_count = 0
    else:
        groups[-1].append(line)
    group_count += 1

for group in groups:
    for item in group[0]:
        if item in group[1] and item in group[2]:
            p2_sum_priorities += get_priority(item)
            break

print(f"P1: {p1_sum_priorities}")
print(f"P2: {p2_sum_priorities}")
