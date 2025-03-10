import string

def count_unique_words(filename):
    """Counts the number of unique words in a text file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()  # Convert text to lowercase
            text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
            words = text.split()  # Split text into words
            unique_words = set(words)  # Store unique words in a set
            return len(unique_words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0

# File names
book1 = 'tom_sawyer.txt'
book2 = 'dorian_gray.txt'

# Count unique words
unique_words_book1 = count_unique_words(book1)
unique_words_book2 = count_unique_words(book2)

# Print results
print(f"Unique words in '{book1}': {unique_words_book1}")
print(f"Unique words in '{book2}': {unique_words_book2}")

# Compare results
if unique_words_book1 > unique_words_book2:
    print(f"Mark Twain used more unique words ({unique_words_book1}) than Oscar Wilde ({unique_words_book2}).")
elif unique_words_book1 < unique_words_book2:
    print(f"Oscar Wilde used more unique words ({unique_words_book2}) than Mark Twain ({unique_words_book1}).")
else:
    print(f"Both authors used the same number of unique words ({unique_words_book1}).")