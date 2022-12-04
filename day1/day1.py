"""
copied from reddit as i couldnt do it.

i removed all the actual \n chars and didn't use split

all the solutions i saw split the file into lists as it was being read
which i didnt see

they all used the double \n\n to split on

I missed split completely
"""


d = [
    sum(map(int, x.split()))
    for x in open("input.txt", "rt").read().strip().split("\n\n")
]
print(max(d), sum(sorted(d)[-3:]))

"""
less complicated version
"""

with open("input.txt") as f:
    f.seek(0)
    rawin = f.read()

elves = rawin.split("\n\n")
sumelves = []

for line in elves:
    intfoods = []
    elf = line.splitlines()
    for food in elf:
        intfoods.append(int(food))
    sumelves.append(sum(intfoods))

sumelves.sort(reverse=True)
print(sum(sumelves[:3]))
