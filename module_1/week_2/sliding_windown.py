def sliding_windown(numb_list, sliding_size):
    result = []

    for i in range(len(numb_list) - sliding_size + 1):
        sub_array = numb_list[i:i+sliding_size]
        max_number_in_sub_array = max(sub_array)
        result.append(max_number_in_sub_array)
    return result


assert sliding_windown([3, 4, 5, 1, -44, 5, 10, 12, 33,
                       1], 3) == [5, 5, 5, 5, 10, 12, 33, 33]
print(sliding_windown([3, 4, 5, 1, -44, 5, 10, 12, 33, 1], 3))
