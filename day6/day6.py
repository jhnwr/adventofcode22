# AOC day 6
# another solution but not a good one
# best solutions do use enumerate and sets compared to lists but
# in a way better way.

with open("input.prod", "r") as f:
    data = f.read()
    data = data.strip()


def check_dupes(lst):
    print("list len:", len(lst), "set len:", len(set(lst)))
    if len(lst) == len(set(lst)):
        print("list len:", len(lst), "set len:", len(set(lst)))
        return True


for x, letter in enumerate(data, start=1):
    #    chunk = [data[x], data[x - 1], data[x - 2], data[x - 3]]
    fat_chunk = [
        data[x],
        data[x - 1],
        data[x - 2],
        data[x - 3],
        data[x - 4],
        data[x - 5],
        data[x - 6],
        data[x - 7],
        data[x - 8],
        data[x - 9],
        data[x - 10],
        data[x - 11],
        data[x - 12],
        data[x - 13],
    ]
    # print("starting letter", x, letter)
    # if check_dupes(chunk) is True:
    #    if x >= 4:
    #        # why am i one down?
    #        print("marker:", x + 1)
    #        print(chunk)
    #        break

    # print("starting letter", x)
    if check_dupes(fat_chunk) is True:
        if x >= 14:
            print("marker:", x + 1)
            print(fat_chunk)
            break

print(len(data))
