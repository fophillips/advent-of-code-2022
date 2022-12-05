from pathlib import Path
import string

VALUES = {chr: val+1 for val, chr in enumerate(string.ascii_letters)}


def solve(data):
    res = 0
    for rucksack in data:
        c_sz = int(len(rucksack) / 2)
        c1 = rucksack[:c_sz]
        c2 = rucksack[c_sz:]
        itm1 = set()
        itm2 = set()
        for itm in c1:
            itm1.add(itm)
        for itm in c2:
            itm2.add(itm)
        common = itm1.intersection(itm2)
        assert len(common) == 1
        res += VALUES[next(iter(common))]
    return res

def solve2(data):
    res = 0
    i = 0
    while i < len(data):
        r1 = set(data[i].strip())
        r2 = set(data[i+1].strip())
        r3 = set(data[i+2].strip())
        common = r1.intersection(r2).intersection(r3)
        assert len(common) == 1
        res += VALUES[next(iter(common))]
        i += 3
    return res



with open(Path(__file__).parent / "input") as f:
    data = f.readlines()

print(solve(data))
print(solve2(data))
