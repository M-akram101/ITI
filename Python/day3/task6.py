import math
from InvertWord.inverted import InvertWord


def Triangle_Sides(s1, s2, s3):

    longest = 0
    side1 = 0
    side2 = 0

    if s1 > s2 and s1 > s3:
        longest = s1
        side1 = s2
        side2 = s3
    elif s2 > s3 and s2 > s1:
        longest = s2
        side1 = s1
        side2 = s3
    elif s3 > s1 and s3 > s2:
        longest = s3
        side1 = s1
        side2 = s2
    else:
        print("1, This is not a right angle triangle")
        return

    if math.sqrt(longest**2) == math.sqrt(((side1**2) + (side2**2))):

        print("This is a right angle triangle")
        return
    print("2,This is not a right angle triangle")


Triangle_Sides(3, 4, 5)
