# Complete the find_longest_word function without a loop. It accepts string inputs, document, and optional longest_word, which is the current longest word and defaults to an empty string.
def find_longest_word(document, longest_word=""):
    # Base case: if the document is empty, return the longest word found so far
    if len(document) == 0:
        return longest_word
    # Split the document into the first word and the rest
    words = document.split(maxsplit=1)
    # If there are no words left, return the longest word found so far
    if len(words) < 1:
        return longest_word
    # Check the first word against the longest word found so far
    first_word = words[0]
    # Update longest_word if the first word is longer
    if len(first_word) > len(longest_word):
        longest_word = first_word
    # If there's only one word left, return the longest word found so far
    if len(words) < 2:
        return longest_word
    # Recur with the rest of the document
    return find_longest_word(words[1], longest_word)