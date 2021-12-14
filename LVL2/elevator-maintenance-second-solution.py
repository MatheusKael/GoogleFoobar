

def solution(l):
    n = len(l)

    for each in range(n):
        l[each] = l[each].split('.')
        for j in range(len(l[each])):
            l[each][j] = int(l[each][j])
        l[each] = tuple(l[each])

    for each in range(n):
        for j in range(n - 1 - each):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    for each in range(n):
        l[each] = '.'.join(map(str, l[each]))

    return l


print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
