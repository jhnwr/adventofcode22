# AOC day 6

with open("input.prod", "r") as f:
    data = f.read()
    data = data.strip()


def check_dupes(lst):
    if len(lst) == len(set(lst)):
        # print("list len:", len(lst), "set len:", len(set(lst)))
        return True


for x, letter in enumerate(data, start=1):
    chunk = [data[x], data[x - 1], data[x - 2], data[x - 3]]
    print("starting letter", x, letter)
    if check_dupes(chunk) is True:
        if x >= 4:
            # why am i one down?
            print("marker:", x + 1)
            print(chunk)
            break
