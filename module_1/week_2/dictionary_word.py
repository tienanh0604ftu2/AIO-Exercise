# Problem

"""
Write a function that reads sentences from a txt file, counts the number of occurrences of each word, and returns a dictionary with the key being the word and the value being the number of times the word appears.
• Input: Path to the txt file
• Output: Dictionary counting the occurrences of each word
"""


def count_words(file_path):
    word_counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.replace('.', '').replace(
                ',', '').replace('-', ' ').lower().split()
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    return word_counts

# testing


file_path = r"module_1/week_2/P1_data.txt"
result = count_words(file_path)
print(result)
