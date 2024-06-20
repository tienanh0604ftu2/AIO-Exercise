# levenshtein distance
"""
Write a program to calculate the minimum Levenshtein edit distance. The Levenshtein distance represents the difference between two strings. The Levenshtein distance between string S and string T is the minimum number of steps to transform string S into string T using three operations:
• Deleting a character
• Adding a character
• Replacing one character with another
This distance is used to calculate the similarity and difference between two strings, such as in the spell checker of Winword. For example, the Levenshtein distance between the two strings "kitten" and "sitting" is 3, because at least 3 transformations are needed. Specifically:
• kitten -> sitten (replace "k" with "s")
• sitten -> sittin (replace "e" with "i")
• sittin -> sitting (add the character "g")

"""


def levenshtein_distance(source, target):
    # Create a matrix to store the distances between prefixes.
    matrix = [[0 for _ in range(len(target) + 1)]
              for _ in range(len(source) + 1)]

    # Initialize the first row and column of the matrix.
    for i in range(len(source) + 1):
        matrix[i][0] = i
    for j in range(len(target) + 1):
        matrix[0][j] = j

    # Fill in the rest of the matrix.
    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,  # deletion
                matrix[i][j - 1] + 1,  # insertion
                matrix[i - 1][j - 1] + cost)  # substitution

    # Return the distance between the full strings.
    return matrix[len(source)][len(target)]


# testing
source = "mother"
target = "father"
print(f"Levenshtein distance between '{source}' and '{
      target}' is {levenshtein_distance(source, target)}")
