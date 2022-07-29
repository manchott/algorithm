import sys
sys.setrecursionlimit(10**6)


def draw_star(n):
    if n == 1:
        return ['*']

    Stars = draw_star(n // 3)
    L = []

    for star in Stars:
        print(star)
        L.append(star*3)
    for star in Stars:
        print(star)
        L.append(star+' '*(n//3)+star)
    for star in Stars:
        print(star)
        L.append(star*3)

    return L


N = int(input())
print('\n'.join(draw_star(N)))
