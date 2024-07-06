
import random

def bionic_reading(text):
    """
    Converts input text to Bionic Reading format by boldening the initial portion of each word.
    """
    result = []
    words = text.split()
    for word in words:
        if len(word) > 1:  # Ensure the word has more than one letter
            # Bolden the first half rounded up of the word
            mid = len(word) // 2 + len(word) % 2
            boldened = '**' + word[:mid] + '**' + word[mid:]
        else:
            boldened = word  # No boldening for single-letter words
        result.append(boldened)
    return ' '.join(result)

# Example usage
sample_text = "This is a sample text to demonstrate the Bionic Reading conversion."
converted_text = bionic_reading(sample_text)
print(converted_text)
