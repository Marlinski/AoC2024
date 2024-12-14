import re
from pydantic import BaseModel
from typing import Optional
import numpy as np

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
    Cost: int


with open(puzzle, 'r') as file:
    pattern = re.compile(
        r"Button A: X\+(\d+), Y\+(\d+)\s+"
        r"Button B: X\+(\d+), Y\+(\d+)\s+"
        r"Prize: X=(\d+), Y=(\d+)"
    )

    data = file.read()
    matches = pattern.findall(data)
    claws = [
        Claw(Ax=int(a_x), Ay=int(a_y), Bx=int(b_x), By=int(b_y),Px=int(prize_x)+10000000000000,Py=int(prize_y)+10000000000000, Solved=False, HitA=0, HitB=0, Cost=0)
        for a_x, a_y, b_x, b_y, prize_x, prize_y in matches
    ]

# we have:
# -------
# ax + by = e   (a in buttonA.x    b is buttonB.x    e is prize.X) 
# cx + dy = f   (c is buttonA.Y    d is buttonB.Y    f is prize.Y)
# 
# we want:
# ------- 
#  x = number of hit on button A
#  y = number of hit on button B
#
# in matrix form:
# --------------
#
#    A      X    =   B
# ( a b ) ( X1 ) _ ( e )
# ( c d ) ( X2 ) ‾ ( f )
#
# Cramer's solution:
# ----------------- 
# X1 = det(A1) / det(A)
# X2 = det(A2) / det(A)
#    
#    A1        A2
# ( e b )   ( a e ) 
# ( f d )   ( c f ) 
# 
# Det(A)  = a*d - b*c
# Det(A1) = e*d - b*f
# Det(A2) = a*f - e*c
def solve_cramer_method(a,b,c,d,e,f):
    det = a * d - b * c
    if det == 0:
        return 0 # no solution

    x1 = (e * d - b * f) // det
    x2 = (a * f - e * c) // det

    if not (a * x1 + b * x2 == e and c * x1 + d * x2 == f):
        return 0 # not an integer solution

    return int(3 * x1 + x2)


print(sum([solve_cramer_method(C.Ax, C.Bx, C.Ay, C.By, C.Px, C.Py) for C in claws]))


# This part was done after to try to use numpy instead of doing hand calculation
#
# A . X = B
# X = B . A^(-1)
#
# SOMEHOW DOES NOT WORK ?!
def solve_inverse_method(a,b,c,d,e,f):
    A = np.array([[a,b],[c,d]])
    B = np.array([e,f])

    if np.linalg.det(A) != 0:
        X = np.linalg.inv(A) @ B
        if np.all(np.isclose(X, np.round(X))):
            return 3*int(X[0]) + int(X[1])
        
    return 0 # not possible

print(sum([solve_inverse_method(C.Ax, C.Bx, C.Ay, C.By, C.Px, C.Py) for C in claws]))

