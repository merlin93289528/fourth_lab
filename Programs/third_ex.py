from math import sqrt


def count_side(ax, ay, bx, by):
    return sqrt((bx - ax) ** 2 + (by - ay) ** 2)


ax, ay = list(map(float, input("Ведіть координати точки А через пробіл: ").split(" ")))
bx, by = list(map(float, input("Ведіть координати точки B через пробіл: ").split(" ")))
cx, cy = list(map(float, input("Ведіть координати точки C через пробіл: ").split(" ")))

side_ab = count_side(ax, ay, bx, by)
side_bc = count_side(bx, by, cx, cy)
side_ac = count_side(ax, ay, cx, cy)

if (side_ab ** 2 < side_ac ** 2 + side_bc ** 2) \
        and (side_ac ** 2 < side_ab ** 2 + side_bc ** 2) \
        and (side_bc ** 2 < side_ac ** 2 + side_ab ** 2):
    print("Трикутник гострокутний")
else:
    print("Трикутник не гострокутний")
