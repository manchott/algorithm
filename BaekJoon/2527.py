for _ in range(4):
    nums = list(map(int, input().split()))
    x1, y1, p1, q1, x2, y2, p2, q2 = nums
    if (x1 > p2 or y1 > q2 or x1 > p2 or y2 > q1 or x2 > p1 or y2 > q2 or x2 > p1 or y1 > q2):
        print('d')
    elif ((x1 == p2 and y1 == q2) or (x1 == p2 and y2 == q1) or (x2 == p1 and y2 == q1) or (x2 == p1 and y1 == q2)):
        print('c')
    elif ((x1 == p2 and y1 != q2) or (x1 == p2 and y2 != q1) or (x2 == p1 and y2 != q1) or (x2 == p1 and y1 != q2) or (x1 != p2 and y1 == q2) or (x1 != p2 and y2 == q1) or (x2 != p1 and y2 == q1) or (x2 != p1 and y1 == q2)):
        print('b')
    else:
        print('a')
