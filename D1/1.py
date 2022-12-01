count = 0
max_1 = 0
max_2 = 0
max_3 = 0

for line in open("1.txt"):
    line = line.strip()
    if line != "":
        count += int(line)
    else:
        if count > max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = count
        elif count > max_2:
            max_3 = max_2
            max_2 = count
        elif count > max_3:
            max_3 = count
        count = 0

print(sum([max_1, max_2, max_3]))
