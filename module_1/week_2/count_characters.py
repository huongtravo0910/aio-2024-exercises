def count_character(string):
    result = {}

    if (string.count(' ') > 0):
        print('Should input one word')
        return
    for char in string:
        result[char] = string.count(char)
    return result


string = "Happiness"

assert count_character(string) == {
    'H': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}
print(count_character('smiles'))
