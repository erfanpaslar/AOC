with open("./input.txt") as f:
    lines = [int(i) for i in f.readlines()]

#part 1
def calc(lines):
    return len([lines[i] for i in range(1, len(lines)) if lines[i]>lines[i-1]])

print(calc(lines)) # 1709

# part 2
print(calc([lines[i]+lines[i+1]+lines[i+2] for i in range(0, len(lines)-2)])) # 1761