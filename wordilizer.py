
import json 


file_dictionary = open("words_dictionary.json")
word_list = json.load(file_dictionary)



# Letters that are green in the right spot
letter_green = ['', '', '', '', '']
# Put letters that are yellow in here
letter_order_yellow = ['', '', '', '', '']
letters_yellow = ''.join(letter_order_yellow)
letters_yellow = ''.join(set(letters_yellow))

# Letters which are black
letters_black = ""

letter_count = 0
for letter in letter_green:
	if not letter == '':
		letter_count += 1
for letter in letters_yellow:
	if not letter == '':
		letter_count += 1

letters_black = list(letters_black)

word_list_valid = []
word_list_scored = {}

longest_words = []

length_count = {}
freq_count = {}

count = 0

for word in word_list:
	try:
		length_count[len(word)] += 1
	except:
		length_count[len(word)] = 1

	if len(word) == 5:
		for letter in word:
			try:
				freq_count[letter] += 1
			except:
				freq_count[letter] = 1

for word in word_list:

	if len(word) == 5:

		valid_count = 0
		invalid = False
		letter_pos = 0

		# Check if letter is not in the word
		for letter in letters_black:
			if letter in word:
				invalid = True;

		if not invalid:
			# Check if there are letters are in right spot 
			position_count = 0
			for letter in letter_green:
				if letter == word[position_count]:
					valid_count += 1
				position_count += 1

			# First check if letter is in word
			for letter in letters_yellow:
				if letter in word:
					valid_count += 1
			
			# Check if letters are in the wrong spot
			position_count = 0
			for position in letter_order_yellow:
				for letter in list(position):
					if letter == word[position_count]:
						invalid = True;
				position_count += 1

		word_letters = {}
		for letter in word:
			try:
				word_letters[letter] += 1
			except:
				word_letters[letter] = 1
			if word_letters[letter] > 1:
				invalid = True;

		if (not invalid) and valid_count == letter_count:
			if (count < 200):
				word_list_valid.append(word)

			word_list_scored[word] = 0
			for letter in word:
				word_list_scored[word] += freq_count[letter]
			count += 1
		letter_pos += 1
	# continue


print(word_list_valid)
print(len(word_list_valid))

# print(length_count)
# print(longest_words)

# print(freq_count)

# from collections import defaultdict
# for w in sorted(freq_count, key=freq_count.get, reverse=True):
#     print(w, freq_count[w])

count = 0
from collections import defaultdict
for w in sorted(word_list_scored, key=word_list_scored.get, reverse=True):
	count += 1
	if count < 10:
		print(w, word_list_scored[w])



file_dictionary.close






