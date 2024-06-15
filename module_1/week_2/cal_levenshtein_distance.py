def cal_levenshtein_distance(source, target):
    m, n = len(source), len(target)

    if m == 0:
        return n
    if n == 0:
        return m

    previous_row = list(range(n + 1))
    current_row = [0] * (n + 1)

    for i in range(1, m + 1):
        current_row[0] = i
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                current_row[j] = previous_row[j - 1]
            else:
                current_row[j] = min(previous_row[j] + 1,
                                     current_row[j - 1] + 1,
                                     previous_row[j - 1] + 1)

        previous_row, current_row = current_row, previous_row

    return previous_row[n]


assert cal_levenshtein_distance("kitten", "sitting") == 3
assert cal_levenshtein_distance("yu", "you") == 1

print(cal_levenshtein_distance("hola", "hello"))
