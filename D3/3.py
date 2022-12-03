def get_priority(item: str) -> int:
    ordinal = ord(item)
    if ordinal > 96:
        return ordinal - 96
    return ordinal - 38


p1_sum_priorities = 0
p2_sum_priorities = 0

# PART 1
for line in open("3.txt"):
    line = line.strip()
    mid = len(line) // 2
    comp_1, comp_2 = line[:mid], line[mid:]
    for item in comp_2:
        if item in comp_1:
            p1_sum_priorities += get_priority(item)
            break

# PART 2
lines = [line for line in open("3.txt")]
i = 0
while i < len(lines):
    for item in lines[i]:
        if item in lines[i + 1] and item in lines[i + 2]:
            p2_sum_priorities += get_priority(item)
            break
    i += 3

print(f"P1: {p1_sum_priorities}")
print(f"P2: {p2_sum_priorities}")
