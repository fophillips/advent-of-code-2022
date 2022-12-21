def solve(data: str):
    i = 0
    while i < len(data) - 14:
        if len(set(data[i:i+14])) == 14:
            return i+14
        i += 1
    

with open("input") as f:
    data = f.read().strip()

print(solve(data))
print(solve("bvwbjplbgvbhsrlpgdmjqwftvncz"))
print(solve("nppdvjthqldpwncqszvftbrmjlhg"))