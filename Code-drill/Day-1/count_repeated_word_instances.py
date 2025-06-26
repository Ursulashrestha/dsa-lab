# Question
# You need to calculate the sum of repeated word instances - that is for any word that appears more than once, count how many extra times it appears beyond the first, and sum all those extra occurrences.

from collections import Counter

def count_repeated_instances(text):
    words = text.split()
    word_count = Counter(words)

    total_repeats = 0
    for word, count in word_count.items():
        if count > 1:
            total_repeats += count - 1
    return total_repeats
