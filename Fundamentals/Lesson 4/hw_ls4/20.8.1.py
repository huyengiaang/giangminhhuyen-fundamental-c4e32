# letter_counts = {}
# for letter in "Mississippi":
#     letter_counts[letter] = letter_counts.get(letter, 0) + 1
# print(letter_counts)

# letter_items = list(letter_counts.items())
# letter_items.sort()
# print(letter_items)

letter_counts = {}
data = input("Enter a sentence: ")  # ask user to enter a sentence

for letter in data:
    if letter != " ":
        letter = letter.lower()     # transform all letters to the same case
        letter_counts[letter] = letter_counts.get(letter,0)+1 
        # count the number of each letter in the sentence

# sort the letters in alphabetical order. 
letter_items = list(letter_counts.items())
letter_items.sort()
print(letter_items)