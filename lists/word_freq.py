#Most frequent word in a list of words in Python
def most_frequent_word(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    max_count = 0
    most_frequent = None
    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_frequent = word

    return most_frequent

# Example usage:
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print("Most frequent word:", most_frequent_word(words))

