import string  # Used to remove punctuations

# Step 1: Ask the user to input a sentence or paragraph
text = input("Enter a sentence or paragraph:\n")

# Step 2: Convert all characters to lowercase to ensures "Hello" and "hello" are counted as the same word
text = text.lower()

# Step 3: Remove punctuation using str.translate and string.punctuation to handles things like ".", ",", "!", etc.
text = text.translate(str.maketrans('', '', string.punctuation))

# Step 4: Split the cleaned text into words. This turns the string into a list of individual words
words = text.split()

# Step 5: Create an empty dictionary to store word frequencies
word_counts = {}

# Step 6: Loop through the list of words and count them
for word in words:
    if word in word_counts:
        word_counts[word] += 1  # If word already seen, increase its count
    else:
        word_counts[word] = 1   # If word is new, add it with a count of 1

# Step 7: Print the word frequencies (unsorted)
print("\n📊 Word Frequencies:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
