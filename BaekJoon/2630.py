# def origami(n):
#     if len(n) == 1:
#         return n[0][0]
#     for i in range(4):

#     origami()
N = 8
a = [[1, 2, 3, 4, 5, 6, 7, 8],
     [9, 10, 11, 12, 13, 14, 15, 16],
     [17, 18, 19, 20, 21, 22, 23, 24],
     [25, 26, 27, 28, 29, 30, 31, 32],
     [33, 34, 35, 36, 37, 38, 39, 40],
     [41, 42, 43, 44, 45, 46, 47, 48],
     [49, 50, 51, 52, 53, 54, 55, 56],
     [57, 58, 59, 60, 61, 62, 63, 64],
     ]


def cut_paper(L):
    count = 0
    n = len(L)
    if n == 1:
        return L[0][0]
    for i in range(2):
        temp = L[(n//2 * i): (n//2 * (i + 1))]

        for j in range(2):
            temp2 = []
            for l in temp:
                temp2.append(l[(n//2 * j): (n//2 * (j + 1))])
                count += 1
            a = cut_paper(temp2)
            print(temp2)

    return count


one = cut_paper(a)
print("one")
print(one)
