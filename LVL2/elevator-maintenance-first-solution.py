

def solution(l):
    n = len(l)

    l = sorted(l)

    for each in range(n):
        l[each] = l[each].split('.')
        for j in range(len(l[each])):
            l[each][j] = int(l[each][j])

    for i in range(n):
        for j in range(n - i-1):

            if len(l[j + 1]) >= 2 and len(l[j]) >= 2:
                if l[j][0] >= l[j+1][0] and l[j][1] > l[j+1][1]:
                    l[j], l[j+1] = l[j+1], l[j]
                elif l[j][0] == l[j+1][0] and l[j][1] == l[j+1][1] and len(l[j]) > len(l[j+1]):
                    l[j+1], l[j] = l[j], l[j+1],
            if len(l[j + 1]) >= 3 and len(l[j]) >= 3:
                if l[j][2] > l[j+1][2] and l[j][1] >= l[j+1][1] and l[j][0] >= l[j+1][0]:
                    l[j], l[j+1] = l[j+1], l[j]

    for i in range(n):
        for j in range(len(l[i])):
            l[i][j] = str(l[i][j])
        l[i] = '.'.join(l[i])

    return l


print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2" ]))


# 0.1, 1.1.1, 1.2, 1.2.1, 1.11, 2, 2.0, 2.0.0
