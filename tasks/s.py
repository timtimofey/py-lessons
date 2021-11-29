def find_longest_word(word_list):
    longest_word = max(word_list, key=len)
    return longest_word


s = ["Я", "люблюhhhh", "собак"]

print(find_longest_word(s))
