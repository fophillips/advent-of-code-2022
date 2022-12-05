from pathlib import Path


def _parse(rnge) -> set:
    s, e = rnge.split("-")
    return set(range(int(s), int(e) + 1))


def solve(data):
    res = 0
    res2 = 0
    for pair in data:
        e1, e2 = pair.strip().split(",")
        s1, s2 = _parse(e1), _parse(e2)
        if s1 <= s2 or s2 <= s1:
            res += 1
        if s1.intersection(s2):
            res2 += 1

    return res, res2


with open(Path(__file__).parent / "input") as f:
    data = f.readlines()

print(solve(data))
