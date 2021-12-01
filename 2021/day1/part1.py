with open("./input.txt") as f:
    lines = f.readlines()
    
print(len([lines[i] for i in range(1, len(lines)) if int(lines[i])>int(lines[i-1]) ]))