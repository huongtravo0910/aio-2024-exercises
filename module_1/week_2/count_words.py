def count_word(text):
    result = {}
    words_list = text.split(' ')
    for letter in words_list:
        if (isinstance(result.get(letter), int) == False):
            result[letter] = 0
        result[letter] += 1
    return result


f = open("module_1/week_2/P1_data.txt", "r")
text = f.read()
f.close()
print(count_word(text)['man'])
