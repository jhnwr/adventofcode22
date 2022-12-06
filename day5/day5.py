"""
This appears to be about moving items from one list to another
but keeping their integrity?

its about parsing, of which i don't really understand
answers seem to use generators. and regex for instructions part
"""

supplies = {
        1: ["R", "S","L","F","Q"],
        2: ["N", "Z", "Q","G","P","T"],
        3: ["S","M","Q","B"],
        4: ["T","G","Z","J","H","C","B","Q"],
        5: ["P","H","M","B","N","F","S"],
        6: ["P","C","Q","N","S","L","V","G"],
        7: ["W","C","F"],
        8: ["Q","H","G","Z","W","V","P","M"],
        9: ["G","Z","D","L","C","N","R"],
    }
with open("input.prod", "r") as f:
    instructions = f.read().splitlines()

# take instruction and remove words

def instructions_to_integers(instruction):
    ins = [c for c in instruction.split()]
    moves = []
    # whats the correct way to dothis?
    for x in ins:
        try:
            moves.append(int(x))
        except:
            pass

    return moves


swap = supplies
for instr in instructions:

    moves = instructions_to_integers(instr)

    times_to_move = moves[0]
    take_from = moves[1]
    give_to = moves[2]

    print("moves:", times_to_move)
    print("take from:", take_from)
    print("give give_to:", give_to)

    for x in range(1, times_to_move +1):
        print(x)
        mover = swap[take_from].pop(-1)
        swap[give_to].append(mover)
        supplies.update(swap)
    swap = supplies
    print(supplies)

print("final", supplies)

for i in supplies.keys():
    print(supplies[i][0])
