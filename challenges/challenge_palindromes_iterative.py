def is_palindrome_iterative(word):
    if word == '':
        return False

    reversed_word = word[len(word)::-1]

    if word == reversed_word:
        return True
    else:
        return False


print(is_palindrome_iterative('asa'))
