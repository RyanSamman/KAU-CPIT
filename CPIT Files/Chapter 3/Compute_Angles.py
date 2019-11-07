import math

x1, y1 = eval(input("First Point (x, y): "))    # 1 is A
x2, y2 = eval(input("Second Point (x, y): "))   # 2 is B
x3, y3 = eval(input("Third Point (x, y): "))    # 3 is C

Triangle = {1: [x1, y1],
            2: [x2, y2],
            3: [x3, y3]}


def length(i1, i2):
    return math.sqrt(
        (Triangle[i2][0]-Triangle[i1][0]) ** 2 +
        (Triangle[i2][1]-Triangle[i1][1]) ** 2)


def angle(i1, i2, i3):
    return math.acos(
        ((Triangle[i1][2] ** 2) - (Triangle[i2][2] ** 2) - (Triangle[i3][2] ** 2)) /
        (-2 * Triangle[i2][2] * Triangle[i3][2]))


a = length(1, 2)
b = length(1, 3)
c = length(2, 3)

Triangle[1] += [a]
Triangle[2] += [b]
Triangle[3] += [c]

B = round(math.degrees(angle(2, 1, 3)), 2)
A = round(math.degrees(angle(1, 2, 3)), 2)
C = round(math.degrees(angle(3, 2, 1)), 2)

Triangle[1] += [A]
Triangle[2] += [B]
Triangle[3] += [C]

print(Triangle)

