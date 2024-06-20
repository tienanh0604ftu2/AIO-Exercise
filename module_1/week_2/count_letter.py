# count letters

"""
Write a function that returns a dictionary counting the number of times each letter appears in a word, with the key being the letter and the value being the number of times it appears.
• Input: A word
• Output: Dictionary counting the occurrences of each letter
• Note: Assume the input words contain only letters from [a-z] or [A-Z]

"""


def count_letter(text):
    letter_counts = {}

    for char in text:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return letter_counts

# testing


strings = "Happiness"
result = count_letter(strings)
print(result)
