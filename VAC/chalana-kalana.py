#CHALANA KALANA PYTHON CODE
import math
def chalana_kalana(a,b,c):
    D=(b**2)-(4*a*c)
    if D<0:
        return "No Real Roots"
    sqrt_D=math.sqrt(D)

    root1=(sqrt_D)/(2*a)
    root2=(-sqrt_D)/(2*a)

    return root1,root2
print(chalana_kalana(1,-5,6))
# CODED BY KRISHA!
