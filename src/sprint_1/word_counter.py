import re


def word_frequency(text):

    text = text.lower()

    text = re.sub(r'[^\w\s]', '', text)

    words = text.split()

    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency