
import json 
import statistics

print_find_next = True
print_length_max = 10

def wordilizer_find_next(word_list, letters_green, letter_order_yellow, letters_black):

	# file_dictionary = open("words_dictionary.json")
	# word_list = json.load(file_dictionary)


	# letters_green = ['', '', '', '', '']
	# letter_order_yellow = ['', '', '', '', '']
	# letters_black = "bif"

	letters_yellow = ''.join(letter_order_yellow)
	letters_yellow = ''.join(set(letters_yellow))
	# letters_yellow = "fb"

	letter_count = 0
	for letter in letters_green:
		if not letter == '':
			letter_count += 1
	for letter in letters_yellow:
		if not letter == '':
			letter_count += 1

	letters_black = list(letters_black)

	word_list_valid = []
	word_list_scored = {}
	word_list_scored["not_multi"] = {}
	word_list_scored["multi"] = {}

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
				for letter in letters_green:
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
						if letter == word[position_count] and letter != letters_green[position_count]:
							invalid = True;
					position_count += 1

			word_letters = {}
			multi_letter = False
			for letter in word:
				try:
					word_letters[letter] += 1
					multi_letter = True;
				except:
					word_letters[letter] = 1

			if (not invalid) and valid_count == letter_count:
				# if (count < 200):
				# 	word_list_valid.append(word)

				if multi_letter:
					multi_letter = "multi"
				else:
					multi_letter = "not_multi"
				
				try:
					word_list_scored[multi_letter][word] = 0
				except:
					word_list_scored[multi_letter] = {}
					word_list_scored[multi_letter][word] = 0
				
				for letter in word:
					word_list_scored[multi_letter][word] += freq_count[letter]

				count += 1
			letter_pos += 1
		# continue


	# print(word_list_valid)
	# print(len(word_list_valid))

	# print(length_count)
	# print(longest_words)

	# print(freq_count)

	# from collections import defaultdict
	# for w in sorted(freq_count, key=freq_count.get, reverse=True):
	#     print(w, freq_count[w])


	# try:
	# 	l1 = l1
	# except:
	# 	# l1 = False
	# 	l1 = []
	# try:
	# 	l2 = l2
	# except:
	# 	# l2 = False
	# 	l2 = []
	# try:
	l1 = sorted(word_list_scored["not_multi"], key=word_list_scored["not_multi"].get, reverse=True)
	l2 = sorted(word_list_scored["multi"], key=word_list_scored["multi"].get, reverse=True)

	if print_find_next:	

		# l2 = []
		for count in range(print_length_max if (len(l1) > print_length_max or len(l2) > print_length_max) else (max(len(l1), len(l2)))):
			if count < len(l1):
				word1 = l1[count]
				word1_score = word_list_scored["not_multi"][l1[count]]
			else:
				word1 = ""
				word1_score = ""
			if count < len(l2):
				word2 = l2[count]
				word2_score = word_list_scored["multi"][l2[count]]
			else:
				word2 = "\t"
				word2_score = "\t"

			print(word1, word1_score, "\t", word2, word2_score)

			# print(word1, word1_score, "\t", word2, word2_score)


	return l1, l2



def wordilizer_sim(word_list, word):


	global print_find_next
	print_find_next = False


	word_listified = list(word)

	attempts = 0
	letters_correct = 0

	letters_green = ['', '', '', '', '']
	letter_order_yellow = ['', '', '', '', '']
	letters_black = ""

	while attempts < 10 and letters_correct != 5:


		[non_multi, multi] = wordilizer_find_next(word_list, letters_green, letter_order_yellow, letters_black)

		if non_multi != []:
			word_guess = non_multi[0]
		elif multi != []:
			word_guess = multi[0]
		else:
			print("fail\t\t", non_multi, multi)
			return attempts, letters_green, letter_order_yellow, letters_black
			
		# print(word_guess)
		# print(non_multi, multi)
		letter_pos = 0
		list(word_guess)
		for i in range(len(word_guess)):
			if word_guess[i] == word_listified[i] and letters_green[i] != word_guess[i]:
				letters_green[i] = word_guess[i]
				letters_correct += 1
			elif word_guess[i] in word and letters_green[i] != word_guess[i]:
				letter_order_yellow[i] += word_guess[i]
			if word_guess[i] not in word:
				letters_black += word_guess[i]

			letter_pos += 1 

		attempts += 1




	return attempts, letters_green, letter_order_yellow, letters_black


 ######  #    #  ######   ####   #    #  #####  ###### 
 #        #  #   #       #    #  #    #    #    #      
 #####     ##    #####   #       #    #    #    #####  
 #         ##    #       #       #    #    #    #      
 #        #  #   #       #    #  #    #    #    #      
 ######  #    #  ######   ####    ####     #    ###### 
                                                       


# # 227 [[T]]hos[[e]]??
# # 228 [M]oist (likely o or t)
# # 229 S[h][[a]]rd (srd)
# # 230 [p]l[e]a[t]
# # 231 aloft

sim_one = False
sim_one = True
if sim_one:	 

	# # Letters that are green in the right spot
	letters_green = ['', '', '', '', '']
	letters_green = ['', '', '', '', '']
	# # Put letters that are yellow in here
	letter_order_yellow = ['', '', '', '', '']
	letter_order_yellow = ['', '', '', '', '']

	# Wrote

	# # Letters which are black
	letters_black = ""
	letters_black = ""


	file_dictionary = open("words_dictionary.json")
	word_list = json.load(file_dictionary)
	[l1, l2] = wordilizer_find_next(word_list, letters_green, letter_order_yellow, letters_black)

	# print(wordilizer_find_next(word_list, letters_green, letter_order_yellow, letters_black))
	# print(wordilizer_sim(word_list, "frame"))
	file_dictionary.close

pass

# # older 3998
# # plier 3889
# # ulcer 3795
# # flier 3752
# # bluer 3599
# # flyer 3506

sim_all = False
# sim_all = True
if sim_all:


	file_dictionary = open("words_dictionary.json")	
	word_list = json.load(file_dictionary)

	# print(wordilizer_sim(word_list, "amiss"))



	all_attempts = []
	all_letters_green = []
	all_letter_order_yellow = []
	all_letters_black = []

	for word in word_list:

		if len(word) != 5:
			continue

		[attempts, letters_green, letter_order_yellow, letters_black] = wordilizer_sim(word_list, word)
		try:
			mean = statistics.mean(all_attempts)
			attempt_max = max(all_attempts)
			attempt_min = min(all_attempts)
		except:
			mean = 0
			attempt_max = 0
			attempt_min = 0

		print (word, attempts, attempt_max, attempt_min, mean, letters_green, letter_order_yellow, letters_black)

		all_attempts.append(attempts)
		all_letters_green.append(letters_green)
		all_letter_order_yellow.append(letter_order_yellow)
		all_letters_black.append(letters_black)


		# print("Sim results:")
		# print(attempts)
		# print(letters_green)
		# print(letter_order_yellow)
		# print(letters_black)



	file_dictionary.close










if 0:
	freq_count = {}

	count = 0
	word_list = ['crane', 'grace', 'drape', 'brace', 'grade', 'grape', 'crave', 'drake', 'frame', 'craze', 'brake', 'grave', 'brave', 'graze']

	for word in word_list:
		if len(word) == 5:
			for letter in word:
				try:
					freq_count[letter] += 1
				except:
					freq_count[letter] = 1
	print(freq_count)