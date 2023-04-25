def quick_sort(string, start, end):
    if start < end:
        p = partition(string, start, end)
        quick_sort(string, start, p - 1)
        quick_sort(string, p + 1, end)


def partition(string, start, end):
    pivot = string[end]
    delimiter = start - 1

    for index in range(start, end):
        if string[index] <= pivot:
            delimiter = delimiter + 1
            string[index], string[delimiter] = string[delimiter], string[index]

    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]

    return delimiter + 1


def is_anagram(first_string, second_string):
    word_lower = list(first_string.lower())
    word_lower2 = list(second_string.lower())

    quick_sort(word_lower, 0, len(word_lower) - 1)
    quick_sort(word_lower2, 0, len(word_lower2) - 1)

    if first_string == "" or second_string == "":
        return ("".join(word_lower), "".join(word_lower2), False)

    return (
        "".join(word_lower),
        "".join(word_lower2),
        word_lower == word_lower2,
    )


print(is_anagram("pedra", "perda"))
