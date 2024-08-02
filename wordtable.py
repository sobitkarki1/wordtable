import nltk
from collections import Counter
import os
import glob

# Download the necessary NLTK data files
nltk.download('punkt')

# Initialize a Counter to hold word counts
word_counts = Counter()

# Process each text file in the current directory
for filename in glob.glob('*.txt'):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        # Tokenize the text into words using NLTK
        words = nltk.word_tokenize(text.lower())
        # Filter out non-alphanumeric tokens
        words = [word for word in words if word.isalnum()]
        # Update the word counts
        word_counts.update(words)

# Get the 10 most common words
most_common_words = word_counts.most_common(10)

# Append the table to the output file
with open('output.log', 'a', encoding='utf-8') as output_file:
    output_file.write(f"{'Word':<15}{'Frequency':<10}\n")
    output_file.write('-' * 25 + '\n')
    for word, frequency in most_common_words:
        output_file.write(f"{word:<15}{frequency:<10}\n")
    output_file.write('\n')  # Add a newline for separation between different runs
