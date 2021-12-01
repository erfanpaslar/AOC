with open("./input.txt") as f:
    lines = [int(i) for i in f.readlines()]

lines = [lines[i]+lines[i+1]+lines[i+2] for i in range(0, len(lines)-2)]

print(len([lines[i] for i in range(1, len(lines)) if int(lines[i])>int(lines[i-1]) ]))
