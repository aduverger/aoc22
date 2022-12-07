for line in open("6.txt"):
    line = line.strip()

for part, char_cnt in enumerate([4, 14]):
    for idx in range(len(line)):
        marker = line[idx : idx + char_cnt]
        if len(marker) == len(set(marker)):
            print(f"P{part}: {idx + char_cnt}")
            break
