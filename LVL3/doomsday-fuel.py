
from fractions import Fraction

# Solution -> Absorbing Markov chain


def replace_probability(m):
    for row in range(len(m)):
        total = 0
        for item in range(len(m[row])):
            total += m[row][item]
        if total != 0:
            for item in range(len(m[row])):
                m[row][item] /= float(total)
    return m


def matrix_multiply(A, B):
    result = []
    dimension = len(A)
    for row in range(len(A)):
        temp = []
        for column in range(len(B[0])):
            product = 0
            for selector in range(dimension):
                product += (A[row][selector]*B[selector][column])
            temp.append(product)
        result.append(temp)
    return result


def transposeMatrix(m):
    return map(list, zip(*m))


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c] * \
            getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant


def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


def matrix_subtraction(A, B):

    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])
    if rowsA != rowsB or colsA != colsB:
        raise ArithmeticError('Matrices are NOT the same size.')

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            C[i][j] = A[i][j] - B[i][j]

    return C


def zeros_matrix(rows, cols):
    m = []
    while len(m) < rows:
        m.append([])
        while len(m[-1]) < cols:
            m[-1].append(0)

    return m


def RQ(m, terminal, non_terminal):
    R = []
    Q = []
    for i in non_terminal:
        temp_t = []
        temp_n = []
        for j in terminal:
            temp_t.append(m[i][j])
        for j in non_terminal:
            temp_n.append(m[i][j])
        R.append(temp_t)
        Q.append(temp_n)
    return R, Q


def identity_matrix(n):
    IdM = zeros_matrix(n, n)
    for i in range(n):
        IdM[i][i] = 1

    return IdM


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def result(m):
    needed = m[0]
    to_fraction = [Fraction(i).limit_denominator() for i in needed]
    lcm = 1
    for i in to_fraction:
        if i.denominator != 1:
            lcm = i.denominator
    for i in to_fraction:
        if i.denominator != 1:
            lcm = lcm*i.denominator/gcd(lcm, i.denominator)

    to_fraction = [(i*lcm).numerator for i in to_fraction]
    to_fraction.append(lcm)

    return to_fraction


def solution(m):

    l = len(m)
    if l == 1:
        if len(m[0]) == 1 and m[0][0] == 0:
            return [1, 1]

    terminal_state = []
    non_terminal_state = []
    for row in range(len(m)):
        count = 0
        for item in range(len(m[row])):
            if m[row][item] == 0:
                count += 1
        if count == l:
            terminal_state.append(row)
        else:
            non_terminal_state.append(row)

    probabilities = replace_probability(m)
    R, Q = RQ(probabilities, terminal_state, non_terminal_state)

    IQ = matrix_subtraction(identity_matrix(len(Q)), Q)

    RQ_inverse = getMatrixInverse(IQ)

    product = matrix_multiply(RQ_inverse, R)

    return result(product)


assert(solution(
    [
        [0],
    ]
)) == [1, 1]

assert(solution(
    [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)) == [7, 6, 8, 21]

assert(solution(
    [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
)) == [0, 3, 2, 9, 14]
