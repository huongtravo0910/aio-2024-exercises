def cal_levenshtein_distance(source, target):
    m, n = len(source), len(target)

    if m == 0:
        return n
    if n == 0:
        return m

    rows, cols = len(source) + 1, len(target) + 1
    matrix = [[i if j == 0 else 0 for j in range(rows)] for i in range(cols)]

    for j in range(rows):
        matrix[0][j] = j

    for i in range(1, cols):
        for j in range(1, rows):
            sub_cost = 0
            if source[j-1] != target[i-1]:
                sub_cost = 1

            matrix[i][j] = min(
                matrix[i-1][j] + 1,
                matrix[i][j-1] + 1,
                matrix[i-1][j-1] + sub_cost
            )

    return matrix[cols-1][rows-1]


assert cal_levenshtein_distance("kitten", "sitting") == 3
assert cal_levenshtein_distance("yu", "you") == 1
assert cal_levenshtein_distance("yu", "") == 2
assert cal_levenshtein_distance("", "you") == 3

print(cal_levenshtein_distance("hola", "hello"))
