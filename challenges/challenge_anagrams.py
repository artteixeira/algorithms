def sort_string(string):
    string_list = list(string.lower())
    sorted_string = ''.join(merge_sort(string_list))
    return sorted_string


def is_anagram(first_string, second_string):
    sorted_first = sort_string(first_string)
    sorted_second = sort_string(second_string)

    compare_strings = sorted_first == sorted_second

    if sorted_first == '' or sorted_second == '':
        compare_strings = False

    return (sorted_first, sorted_second, compare_strings)


def merge_sort(string_list):
    if len(string_list) <= 1:
        return string_list

    mid = len(string_list) // 2
    left = string_list[:mid]
    right = string_list[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
