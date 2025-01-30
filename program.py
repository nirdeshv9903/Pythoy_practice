# Longest Palindromic Substring
# Write a program to find the longest palindromic substring in a given string.
input_string = "babad"
def substring(input_string):
    def expand_around_center(left, right):
        while left >= 0 and right < len(input_string) and input_string[left] == input_string[right]:
            left -= 1
            right += 1
        return input_string[left + 1:right]
    if len(input_string) == 0:
        return ""
    longest = ""
    for i in range(len(input_string)):
        # odd length
        palindrome_odd = expand_around_center(i, i)
        # even length
        palindrome_even = expand_around_center(i, i + 1)
        longest = max(longest, palindrome_odd, palindrome_even, key=len)
    return longest
print(substring(input_string))
# Input: "babad"
# Output: "bab" or "aba"

# Character Frequency Analysis
# Write a function to find the character that appears the most in a string, ignoring case and spaces.
st = "This is a test sentence"
def character_frequency_analysis(st):
    st = st.replace(" ", "").lower()
    max_char = ""
    max_count = 0
    for char in st:
        if st.count(char) > max_count:
            max_char = char
            max_count = st.count(char)
    return {'Character': max_char, 'Frequency': max_count}
print(character_frequency_analysis(st))
# Input: "This is a test sentence"
# Output: {'Character': 't', 'Frequency': 4}

# String Compression
# Implement a function to compress a string by representing repeated characters with counts.
st1 = "aaabbccca"
def string_compression(st1):
    compressed = ""
    count = 1
    for i in range(len(st1) - 1):
        if st1[i] == st1[i + 1]:
            count += 1
        else:
            compressed += st1[i] + str(count)
            count = 1
    compressed += st1[-1] + str(count)
    return compressed
print(string_compression(st1))
# Input: "aaabbccca"
# Output: "a3b2c3a1"

# Find Anagrams
# Write a function to find all the anagrams of a word in a list of strings.
word = "listen"
lst = ["enlist", "google", "inlets", "banana"]
def find_anagrams(word, lst):
    anagrams = []
    for w in lst:
        if sorted(word) == sorted(w):
            anagrams.append(w)
    return anagrams
print(find_anagrams(word, lst))
# Input: word='listen', lst=['enlist', 'google', 'inlets', 'banana']
# Output: ['enlist', 'inlets']

# Caesar Cipher Decoder
# Implement a Caesar cipher decryption function for a given encoded string and a shift value.
cipher = "dwwdfn"
shift = 3
def caesar_cipher_decoder(cipher, shift):
    decoded = ""
    for char in cipher:
        decoded += chr((ord(char) - shift - 97) % 26 + 97)
    return decoded
print(caesar_cipher_decoder(cipher, shift))
# Input: cipher='dwwdfn', shift=3
# Output: "attack"