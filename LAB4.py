def move(peg1, peg2, name1, name2):
    if not peg1:
        disk = peg2.pop()
        peg1.append(disk)
        print("Move disk", disk, "from", name2, "to", name1)
    elif not peg2:
        disk = peg1.pop()
        peg2.append(disk)
        print("Move disk", disk, "from", name1, "to", name2)
    elif peg1[-1] < peg2[-1]:
        disk = peg1.pop()
        peg2.append(disk)
        print("Move disk", disk, "from", name1, "to", name2)
    else:
        disk = peg2.pop()
        peg1.append(disk)
        print("Move disk", disk, "from", name2, "to", name1)


n = int(input("Enter number of disks: "))

pegs = {
    "A": list(range(n, 0, -1)),
    "B": [],
    "C": []
}

if n % 2 == 0:
    order = [("A", "B"), ("A", "C"), ("B", "C")]
else:
    order = [("A", "C"), ("A", "B"), ("B", "C")]

total_moves = 2 ** n - 1

for i in range(total_moves):
    first, second = order[i % 3]
    move(pegs[first], pegs[second], first, second)

print("Solved in", total_moves, "moves")
