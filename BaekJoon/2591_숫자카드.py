C = input()
S = [1]
if int(C[0:2]) < 35 and C[1] != '0':
    S.append(2)
else:
    S.append(1)
for i in range(2, len(C)):
    if C[i] == '0':
        S.append(S[i - 2])
        continue
    S.append(S[i - 1])
    if int(C[i - 1: i + 1]) < 35 and C[i - 1] != '0':
        S[i] += S[i - 2]
print(S[-1])
