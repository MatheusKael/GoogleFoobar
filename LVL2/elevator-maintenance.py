

def solution(l):
    n = len(l)

    for each in range(n):
        l[each] = l[each].split('.')

    for index, i in enumerate(l):

        for j in range(len(l[index])):

            # Major
            if index + 1 < len(l):
                if j == 0:
                    if l[index][j] > l[index + 1][j]:
                        l[index], l[index + 1] = l[index + 1], l[index]

    print(l)


print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
