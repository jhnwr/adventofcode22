with open("input.prod", "r") as f:
    input = []
    data = f.read().splitlines()
    for item in data:
        input.append(tuple(item.split(",")))


# part 1
results = []
for assign in input:
    pair = []
    pair2 = []
    print(assign)
    split_assign = assign[0].split("-")
    split_assign1 = assign[1].split("-")
    for x in range(int(split_assign[0]), int(split_assign[1])+1):
        # print(split_ass, x)
        pair.append(x)
    for x in range(int(split_assign1[0]), int(split_assign1[1])+1):
        # print(split_ass1, x)
        pair2.append(x)
    results.append((pair, pair2))

counter = 0
for item in results:
    if set(item[1]).issubset(item[0]) or set(item[0]).issubset(item[1]):
        print(item)
        counter += 1

print("part1:", counter)

p2counter = 0
for item in results:
    for x in item[0]:
        if x in item[1]:
            print(x)
            p2counter += 1
            break

print("part2:", p2counter)
