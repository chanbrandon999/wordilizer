
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
letters_black = "pens"

letter_count = 0
for letter in letter_green:
	if not letter == '':
		letter_count += 1
for letter in letters_yellow:
	if not letter == '':
		letter_count += 1

letters_black = list(letters_black)

word_list_valid = []

count = 0
for word in word_list:
	if (count < 200):
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

			if (not invalid) and valid_count == letter_count:
				word_list_valid.append(word)
				count += 1
			letter_pos += 1
	# continue


print(word_list_valid)
print(len(word_list_valid))





file_dictionary.close






