# Дано множество А из N точек(N>2, точки заданы свомим коорадинатами х, у).
# Найти такую точку из данного множества, сумма расстояний
# от которой до остальных его точек минимальна, и саму эту сумму.
import itertools
def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
def total_distance(point, points):
    return sum(distance(point, p) for p in points)
def find_min_total_distance(points):
    min_total_dist = float('inf')
    min_point = None
    for p in points:
        dist = total_distance(p, points)
        if dist < min_total_dist:
            min_total_dist = dist
            min_point = p
        return min_point, min_total_dist

N = 4
points = [(1, 1), (2, 4), (5, 2), (7, 3)]
min_point, min_total_dist = find_min_total_distance(points)
print(f"Точка {min_point} имеет минимальную сумму расстояний до остальных точек: {min_total_dist}")