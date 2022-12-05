from dataclasses import dataclass
from typing import List

"""
[M] [H]         [N]                
[S] [W]         [F]     [W] [V]    
[J] [J]         [B]     [S] [B] [F]
[L] [F] [G]     [C]     [L] [N] [N]
[V] [Z] [D]     [P] [W] [G] [F] [Z]
[F] [D] [C] [S] [W] [M] [N] [H] [H]
[N] [N] [R] [B] [Z] [R] [T] [T] [M]
[R] [P] [W] [N] [M] [P] [R] [Q] [L]
 1   2   3   4   5   6   7   8   9 
 """

State = List[List[str]]
INITIAL_STATE = [
    ["R", "N", "F", "V", "L", "J", "S", "M"],
    ["P", "N", "D", "Z", "F", "J", "W", "H"],
    ["W", "R", "C", "D", "G"],
    ["N", "B", "S"],
    ["M", "Z", "W", "P", "C", "B", "F", "N"],
    ["P", "R", "M", "W"],
    ["R", "T", "N", "G", "L", "S", "W"],
    ["Q", "T", "H", "F", "N", "B", "V"],
    ["L", "M", "H", "Z", "N", "F"],
]


@dataclass
class Action:
    amount: int
    fro: int
    to: int


def _parse_line(line: str) -> Action:
    _, amount, _, fro, _, to = line.strip().split()
    return Action(int(amount), int(fro), int(to))


def _apply_action(state: State, action: Action):
    to_move = reversed(state[action.fro - 1][-1 * action.amount :])
    state[action.fro - 1] = state[action.fro - 1][: -1 * action.amount]
    state[action.to - 1].extend(to_move)


def solve(state: State, actions: List[Action]) -> str:
    for action in actions:
        _apply_action(state, action)
    return "".join(col[-1] for col in state)


with open("input") as f:
    actions = [_parse_line(line) for line in f]

print(solve(INITIAL_STATE, actions))
