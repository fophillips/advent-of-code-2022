def top3():
    with open("input") as f:
        data = f.readlines()

    cur = 0
    top = (0, 0, 0)
    for l in data:
        if l.strip() == "":
            if cur > top[0]:
                if cur > top[1]:
                    if cur > top[2]:
                        top = (top[1], top[2], cur)
                    else:
                        top = (top[1], cur, top[2])
                else:
                    top = (cur, top[1], top[2])
            cur = 0
        else:
            cur += int(l)
    return top

def solve1(t):
    return t[2]

def solve2(t):
    return sum(t)
if __name__ == "__main__":
    t = top3()
    print(solve1(t))
    print(solve2(t))