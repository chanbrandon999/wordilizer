

import json 


file_dictionary = open("words_dictionary.json")
word_list = json.load(file_dictionary)

letter_list = ['r', 'u', 'w', 'g']
# letter_list = ['r', 'u', 'w', 'g', '']
word_list_valid = []

count = 0
for word in word_list:
	if (count < 100):
		if len(word) == 5:
			valid_count = 0
			for letter in letter_list:
				if letter in word:
					valid_count += 1
					if valid_count == len(letter_list):
						# print(word)
						word_list_valid.append(word)
						count += 1
	# continue


print(word_list_valid)





file_dictionary.close






