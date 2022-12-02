SCORE = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3
}

YOURS = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS"
}

MINE = {
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS"
}

WIN = {
    "ROCK": "PAPER",
    "PAPER": "SCISSORS",
    "SCISSORS": "ROCK"
}

LOSE = {v: k for k, v in WIN.items()}

def calculate_score(yours, mine):
    if yours == mine:
        win = 3
    else:
        if mine == WIN[yours]:
            win = 6
        else:
            win = 0
    return win + SCORE[mine]

def solve1():
    with open("input") as f:
        rounds = f.readlines()
    score = 0
    for round in rounds:
        y, m = round.split()
        yours, mine = YOURS[y], MINE[m]
        score += calculate_score(yours, mine)

    return score

def solve2():
    with open("input") as f:
        rounds = f.readlines()
    score = 0
    for round in rounds:
        y, result = round.split()
        yours = YOURS[y]
        if result == "X":
            mine = LOSE[yours]
        elif result == "Y":
            mine = yours
            score += 3
        else:
            mine = WIN[yours]
            score += 6

        score += SCORE[mine]

    return score

print(solve1())
print(solve2())