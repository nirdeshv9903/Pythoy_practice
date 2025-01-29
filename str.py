# I am using lates version of python 3.13.1

text = "Python Programming"
# Extract the first character.
print(text[0])
# Extract the last character.
print(text[-1])
# Extract the 7th character from the string.
print(text[7]) # P
print(text[6]) # " "

# Slicing:
# Extract the substring "Python" from text.
print(text[0:6])
# Extract the substring "Programming" from text.
print(text[7:])
# Extract every alternate character from the string.
print(text[::2])
# Reverse the string using slicing.
print(text[::-1])

# Nested Indexing:
nested_text = "Learn Python [Basics]"

# Extract the substring "Basics" using slicing.
print(nested_text[14:19])
# Extract the square brackets ([]) along with the word "Basics".
print(nested_text[12:21])

# Built-in Methods
# String Length:
sentence = "Data Analytics using Python"
# Write a program to find the length of the string:
print(len(sentence)) # it will includ the spaces

# Changing Case:
h = "hello world"
# Convert the string "hello world" to uppercase.
print(h.upper())
# Convert "PYTHON IS FUN" to lowercase.
h1 = "PYTHON IS FUN"
print(h1.lower())
# Capitalize the first letter of "machine learning".

# Finding and Replacing:
quote = "The quick brown fox jumps over the lazy dog"
print(quote)
# Find the index of the substring "fox".
print(quote.find("fox"))
# Replace "lazy dog" with "active cat".
print(quote.replace("lazy dog", "active cat"))

# String Splitting and Joining:
# Given the string:
words = "apple,banana,cherry"
# Split the string into a list of words.
print(words.split(","))
# Join the words back into a string separated by spaces
print(" ".join(words.split(",")))
print("Extracting the first character.")
print(text[0])
print("Extracting the last character.")
print(text[-1])
print("Extracting the 7th character from the string.")
print(text[7]) # P
print("Extracting the 6th character from the string.")
print(text[6]) # " "

print("Slicing:")
print("Extracting the substring 'Python' from text.")
print(text[0:6])
print("Extracting the substring 'Programming' from text.")
print(text[7:])
print("Extracting every alternate character from the string.")
print(text[::2])
print("Reversing the string using slicing.")
print(text[::-1])

print("Nested Indexing:")
print("Extracting the substring 'Basics' using slicing.")
print(nested_text[14:19])
print("Extracting the square brackets ([]) along with the word 'Basics'.")
print(nested_text[12:21])

print("Built-in Methods")
print("String Length:")
print("Finding the length of the string:")
print(len(sentence)) # it will include the spaces

print("Changing Case:")
print("Converting the string 'hello world' to uppercase.")
print(h.upper())
print("Converting 'PYTHON IS FUN' to lowercase.")
print(h1.lower())
print("Capitalizing the first letter of 'machine learning'.")
print("machine learning".capitalize())

print("Finding and Replacing:")
print("Original quote:")
print(quote)
print("Finding the index of the substring 'fox'.")
print(quote.find("fox"))
print("Replacing 'lazy dog' with 'active cat'.")
print(quote.replace("lazy dog", "active cat"))

print("String Splitting and Joining:")
print("Splitting the string into a list of words.")
print(words.split(","))
print("Joining the words back into a string separated by spaces")
print(" ".join(words.split(",")))

# Checking Membership:

# Check if the substring "Python" exists in the string "Learn Python Programming".
py = "Python"
py_str = "Learn Python Programming"
print(py in py_str)
# Check if the string starts with "Learn" and ends with "Programming".

# Whitespace Removal:
# Given the string:

messy_text = "   Clean this text    "
# Remove leading whitespace.
print(messy_text.lstrip())
# Remove trailing whitespace.
print(messy_text.rstrip())
# Remove both leading and trailing whitespace.
print(messy_text.strip())

# Counting Substrings:
# Given the string:
paragraph = "Python is powerful. Python is versatile. Python is easy to learn."
# Count the occurrences of the word "Python".
print(paragraph.count("Python"))
# Count the occurrences of the letter "i"
print(paragraph.count("i"))

# String Palindrome:
# Write a program to check if the string "madam" is a palindrome.
palindrome = "madam"
print(palindrome == palindrome[::-1])

# Anagram Checker:
# Write a function to check if the strings "listen" and "silent" are anagrams.
def anagram_checker(str1, str2):
    return sorted(str1) == sorted(str2)
print(anagram_checker("listen", "silent"))

# Word Frequency:
# Given a sentence:
sentence = "the quick brown fox jumps over the lazy dog"
# Count the number of times each word appears in the sentence.
word_freq = {}
for word in sentence.split():
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print(word_freq)

# Extract Digits and Letters:
# Given a string:

mixed_string = "Python3.8 is awesome!"
# Extract all the digits (3.8) from the string.
print(mixed_string[6:9])
# Extract all the alphabetic characters.
print("".join([char for char in mixed_string if char.isalpha()])) # list comperehension

# Remove Special Characters:
print(mixed_string[-1])

special_text = "Hello@$%& World!!!"
# Write a program to remove all special characters from the string:
print("".join([char for char in special_text if char.isalnum()]))
