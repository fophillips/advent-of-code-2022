from dataclasses import dataclass
import string
from typing import List, Tuple

DIGITS = tuple(string.digits)
LIMIT = 100_000
TO_DELETE = 30_000_000

@dataclass
class Directory:
    name: str
    dirs: List['Directory']
    size: int
    parent: 'Directory'

def solve(lines: List[str]) -> Tuple[int]:
    root = Directory("/", [], 0, None)
    result = []
    cwd = root
    for line in lines[1:]:
        if line.startswith("$ cd"):
            name = line.split()[2]
            if name == "..":
                if cwd.size <= LIMIT:
                    result.append(cwd)
                cwd.parent.size += cwd.size
                cwd = cwd.parent
            else:
                dir = Directory(name, [], 0, cwd)
                cwd.dirs.append(dir)
                cwd = dir
        elif line.startswith(DIGITS):
            size = int(line.split()[0])
            cwd.size += size
    while cwd.parent:
        if cwd.size <= LIMIT:
            result.append(cwd)
        cwd.parent.size += cwd.size
        cwd = cwd.parent
    return sum(d.size for d in result)

with open("input_test") as f:
    lines = f.readlines()

print(solve(lines))
