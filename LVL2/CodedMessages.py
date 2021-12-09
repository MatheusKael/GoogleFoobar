
def solution(l):
    s = sum(l)
    lSorted = sorted(l)
    queue1 = []
    queue2 = []
    queue3 = []

    if(s == 0):
        return 0

    for i in lSorted:
        if(i % 3 == 0):
            queue1.append(i)
        elif(i % 3 == 1):
            queue2.append(i)
        elif(i % 3 == 2):
            queue3.append(i)

    if(s % 3 == 0):
        lSorted = sorted(lSorted, reverse=True)

        stringTransformed = [str(digit) for digit in lSorted]

        return "".join(stringTransformed)
    elif(s % 3 == 1):
        queue2 = sorted(queue2, reverse=True)

        if(len(queue2) > 0):
            queue2.pop()
        else:
            queue3 = sorted(queue3, reverse=True)
            if(len(queue3) > 0):
                queue3.pop()
            if(len(queue3) > 0):
                queue3.pop()
    elif(s % 3 == 2):
        queue3 = sorted(queue3, reverse=True)
        if(len(queue3) > 0):
            queue3.pop()
        else:

            queue2 = sorted(queue2, reverse=True)
            if(len(queue2) > 0):
                queue2.pop()
            if(len(queue2) > 0):
                queue2.pop()

    lSorted = sorted(queue1 +
                     queue2 + queue3, reverse=True)

    stringTransformed = [str(digit) for digit in lSorted]
    if(len(stringTransformed) > 1):
        return "".join(stringTransformed)

    return 0


print(solution([4, 3, 1, 2]))
