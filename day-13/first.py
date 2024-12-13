import re
from pydantic import BaseModel
from typing import Optional

puzzle = 'day-13/puzzle'

class Claw(BaseModel):
    Ax: int
    Ay: int
    Bx: int
    By: int
    Px: int
    Py: int
    Solved: bool
    HitA: Optional[int]
    HitB: Optional[int]

with open(puzzle, 'r') as file:
    pattern = re.compile(
        r"Button A: X\+(\d+), Y\+(\d+)\s+"
        r"Button B: X\+(\d+), Y\+(\d+)\s+"
        r"Prize: X=(\d+), Y=(\d+)"
    )

    data = file.read()
    matches = pattern.findall(data)
    claws = [
        Claw(Ax=a_x, Ay=a_y, Bx=b_x, By=b_y,Px=prize_x,Py=prize_y, Solved=False, HitA=101, HitB=101)
        for a_x, a_y, b_x, b_y, prize_x, prize_y in matches
    ]


for claw in claws:
    for HA in range(101):
        HB = int((claw.Px - claw.Ax * HA) / claw.Bx)
        if (HB <= 100) and (HA*claw.Ax + HB*claw.Bx == claw.Px) and (HA*claw.Ay + HB*claw.By == claw.Py) and (3*HA+HB) < (3*claw.HitA + claw.HitB):
            claw.Solved = True
            claw.HitA = HA
            claw.HitB = HB
            break

print(sum([3*claw.HitA + 1*claw.HitB if claw.Solved else 0 for claw in claws]))
    