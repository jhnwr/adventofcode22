with open("input.txt", "r") as f:
    data = f.read().splitlines()

# bit of a mess but at least i got the right answers

matching_items = []

for item in data:
    first, second = item[:len(item) // 2], item[len(item) // 2:]
    # print("first:", first, "second:", second)
    for char in first:
        if char in second:
            # print("found", char, "in", second)
            matching_items.append(char)
            break

# print(matching_items)
# print(len(matching_items))
# print(len(data))

priority_value = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}

total = sum([priority_value[letter] for letter in matching_items])

print("PART1:", total)

# part 2

# split data list into chunks of 3

elfchunk = [data[x: x + 3] for x in range(0, len(data), 3)]

chunky_match = []

for elf in elfchunk:
    f, s, t = elf[0], elf[1], elf[2]
    # print(f, s, t)
    for c in f:
        if c in s:
            if c in t:
                chunky_match.append(c)
                # print(c)
                break

# print(len(chunky_match))
total2 = sum([priority_value[letter] for letter in chunky_match])
print("PART2:", total2)
