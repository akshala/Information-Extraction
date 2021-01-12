import nltk
from pprint import pprint
import re
from nltk.tokenize import RegexpTokenizer
from num2words import num2words

def read_file(file_name):
# reading file into a string
	with open(file_name) as file:
		text = file.read() 
	return text

def first(file_name):
#  sentences and word count
	text = read_file(file_name)
	text = text.split('\n\n') 
	sentences = []
	for elt in text:
		# removing special characters with space
		elt = elt.replace('\n', ' ')
		elt = elt.replace('-', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('*', ' ')
		elt = elt .replace('#', ' ')
		elt = elt.replace('+', ' ')
		elt = elt.replace('^', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('>', ' ')
		elt = elt.replace('=', ' ')
		elt = elt.replace('|', ' ')
		elt = elt.strip()  # removing extra space at start and end
		initial = nltk.sent_tokenize(elt)   # tokenize to sentences
		for sub_elt in initial:
			sub_elt = re.sub(' +',' ',sub_elt)  # replace multiple spaces with a single space
			sentences.append(sub_elt)
	print('sentence count:', len(sentences))
	words = []
	tokenizer = RegexpTokenizer('\w+')  # '/w+' matches word characters equal to [a-zA-Z0-9_]
	for elt in sentences:
		filterdText = tokenizer.tokenize(elt)  # split sentences to words
		for sub_elt in filterdText:
			if not sub_elt.isnumeric():  # numeric word not added to list
				words.append(sub_elt)
	print('word count:', len(words))

def second(file_name):
#  words starting with vowels and consonants
	text = read_file(file_name)
	text = text.split('\n\n') 
	sentences = []
	for elt in text:
		# removing special characters with space
		elt = elt.replace('\n', ' ')
		elt = elt.replace('-', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('*', ' ')
		elt = elt .replace('#', ' ')
		elt = elt.replace('+', ' ')
		elt = elt.replace('^', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('>', ' ')
		elt = elt.replace('=', ' ')
		elt = elt.replace('|', ' ')
		elt = elt.strip()  # removing extra space at start and end
		initial = nltk.sent_tokenize(elt)   # tokenize to sentences
		for sub_elt in initial:
			sub_elt = re.sub(' +',' ',sub_elt)  # replace multiple spaces with a single space
			sentences.append(sub_elt)
	
	words = []
	tokenizer = RegexpTokenizer('\w+')  # '/w+' matches word characters equal to [a-zA-Z0-9_]
	for elt in sentences:
		filterdText = tokenizer.tokenize(elt)  # split sentences to words
		for sub_elt in filterdText:
			if not sub_elt.isnumeric():  # numeric word not added to list
				words.append(sub_elt)
	vowels = []
	consonants = []
	regex = '^[aeiouAEIOU]'   # regex to match vowels
	for elt in words:
		if re.search(regex, elt):
			vowels.append(elt)
		else:
			consonants.append(elt)  # if vowel regex doesn't match then word starts with consonant
	print('Count of words starting with consonants:', len(consonants))
	print('Count of words starting with vowels:', len(vowels))

def third(file_name):
# email IDs
	text = read_file(file_name)
	text = text.split('\n\n') 
	sentences = []
	for elt in text:
		# removing special characters with space
		elt = elt.replace('\n', ' ')
		elt = elt.replace('-', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('*', ' ')
		elt = elt .replace('#', ' ')
		elt = elt.replace('+', ' ')
		elt = elt.replace('^', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('>', ' ')
		elt = elt.replace('=', ' ')
		elt = elt.replace('|', ' ')
		elt = elt.strip()  # removing extra space at start and end
		initial = nltk.sent_tokenize(elt)   # tokenize to sentences
		for sub_elt in initial:
			sub_elt = re.sub(' +',' ',sub_elt)  # replace multiple spaces with a single space
			sentences.append(sub_elt)
	emails = []
	for elt in sentences:
		email_ID = re.findall('\S+@\S+', elt)  # email ID should have @
		if len(email_ID) > 0:
			emails.extend(email_ID)
	print(emails)

def fourth(file_name, word):
# sentences starting with given word
	text = read_file(file_name)
	text = text.split('\n\n') 
	sentences = []
	for elt in text:
		# removing special characters with space
		elt = elt.replace('\n', ' ')
		elt = elt.replace('-', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('*', ' ')
		elt = elt .replace('#', ' ')
		elt = elt.replace('+', ' ')
		elt = elt.replace('^', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('>', ' ')
		elt = elt.replace('=', ' ')
		elt = elt.replace('|', ' ')
		elt = elt.strip()  # removing extra space at start and end
		initial = nltk.sent_tokenize(elt)   # tokenize to sentences
		for sub_elt in initial:
			sub_elt = re.sub(' +',' ',sub_elt)  # replace multiple spaces with a single space
			sentences.append(sub_elt)
	target = []
	word = word.lower()  # lower case word to find
	regex = '^' + word  # regex for sentence starting with given word
	for elt in sentences:
		lower_case = elt.lower()  # lowercase the string
		if re.search(regex, lower_case):
			target.append(elt)
		lower_case = re.sub(r"(\d+)", lambda x: num2words(int(x.group())), lower_case)  # converting number to word
		if re.search(regex, lower_case):
			target.append(elt)

	print('Count of sentences starting with word', word, ':', len(target))
	print('The sentences are as follows:')
	for elt in target:
		print('->', elt)

def fifth(file_name, word):
# sentences ending with given word
	text = read_file(file_name)
	text = text.split('\n\n') 
	sentences = []
	for elt in text:
		# removing special characters with space
		elt = elt.replace('\n', ' ')
		elt = elt.replace('-', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('*', ' ')
		elt = elt .replace('#', ' ')
		elt = elt.replace('+', ' ')
		elt = elt.replace('^', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('>', ' ')
		elt = elt.replace('=', ' ')
		elt = elt.replace('|', ' ')
		elt = elt.strip()  # removing extra space at start and end
		initial = nltk.sent_tokenize(elt)   # tokenize to sentences
		for sub_elt in initial:
			sub_elt = re.sub(' +',' ',sub_elt)  # replace multiple spaces with a single space
			sentences.append(sub_elt)
	target = []
	word = word.lower()  # lowercase word to find
	regex = word + '[\.!\?*]' + '$'  # regex for sentence ending with given word
	for elt in sentences:
		lower_case = elt.lower()   # lowercase the string
		if re.search(regex, lower_case):
			target.append(elt)
	lower_case = re.sub(r"(\d+)", lambda x: num2words(int(x.group())), lower_case)  # converting number to word
	if re.search(regex, lower_case):
		target.append(elt)

	print('Count of sentences ending with word', word, ':', len(target))
	print('The sentences are as follows:')
	for elt in target:
		print('->', elt)

def sixth(file_name, word):
# sentences containg given word
	text = read_file(file_name)
	text = text.split('\n\n') 
	sentences = []
	for elt in text:
		# removing special characters with space
		elt = elt.replace('\n', ' ')
		elt = elt.replace('-', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('*', ' ')
		elt = elt .replace('#', ' ')
		elt = elt.replace('+', ' ')
		elt = elt.replace('^', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('>', ' ')
		elt = elt.replace('=', ' ')
		elt = elt.replace('|', ' ')
		elt = elt.strip()  # removing extra space at start and end
		initial = nltk.sent_tokenize(elt)   # tokenize to sentences
		for sub_elt in initial:
			sub_elt = re.sub(' +',' ',sub_elt)  # replace multiple spaces with a single space
			sentences.append(sub_elt)
	target = []
	word = word.lower() # lowercase target word
	for elt in sentences:
		lower_case = elt.lower()  # lowercase the string
		if lower_case.find(word) != -1:  # find target word in sentence
			target.append(elt)
		lower_case = re.sub(r"(\d+)", lambda x: num2words(int(x.group())), lower_case)  # converting number to word
		# if re.search(regex, lower_case):
		# 	target.append(elt)
	print('Countount of sentences containing the word', word, ':', len(target))
	print('The sentences are as follows:')
	for elt in target:
		print('->', elt)

def seventh(file_name):
# questions
	text = read_file(file_name)
	text = text.split('\n\n') 
	sentences = []
	for elt in text:
		# removing special characters with space
		elt = elt.replace('\n', ' ')
		elt = elt.replace('-', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('*', ' ')
		elt = elt .replace('#', ' ')
		elt = elt.replace('+', ' ')
		elt = elt.replace('^', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('>', ' ')
		elt = elt.replace('=', ' ')
		elt = elt.replace('|', ' ')
		elt = elt.strip()  # removing extra space at start and end
		initial = nltk.sent_tokenize(elt)   # tokenize to sentences
		for sub_elt in initial:
			sub_elt = re.sub(' +',' ',sub_elt)  # replace multiple spaces with a single space
			sentences.append(sub_elt)
	target = []
	regex = '[\?+]' + '$'  # regex for sentence ending with one or more question mark
	for elt in sentences:
		if re.search(regex, elt):
			if elt.find('\n') != 0:  # if there are \n characters present in the string then split it
				elt = elt.split('\n')
				target.append(elt[-1])  # the last of this list would be used
			else:
				target.append(elt)
	print('Questions present in the file are as follows:')
	if len(target) == 0:
		print('No questions present in file')
	else:
		for elt in target:
			print('->', elt)

def eighth(file_name):
# minutes and seconds
	text = read_file(file_name)
	text = text.split('\n\n') 
	sentences = []
	for elt in text:
		# removing special characters with space
		elt = elt.replace('\n', ' ')
		elt = elt.replace('-', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('*', ' ')
		elt = elt .replace('#', ' ')
		elt = elt.replace('+', ' ')
		elt = elt.replace('^', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('>', ' ')
		elt = elt.replace('=', ' ')
		elt = elt.replace('|', ' ')
		elt = elt.strip()  # removing extra space at start and end
		initial = nltk.sent_tokenize(elt)   # tokenize to sentences
		for sub_elt in initial:
			sub_elt = re.sub(' +',' ',sub_elt)  # replace multiple spaces with a single space
			sentences.append(sub_elt)
	target = ''
	for elt in sentences:
		if elt.find('Date') != -1:  # find the sentence containing the word date
			target = elt
			break
	target = target.split()  # this is then split into words using spaces as a delimiter
	gmt_index = target.index('GMT')  # find the word GMT
	time = target[gmt_index-1]  # time would be present in the word before GMT
	time = time.split(':')   # split the time word on basis of :
	minutes = time[1] # the first index will have minutes
	seconds = time[2]  # the second index will have seconds
	print(minutes, 'min,', seconds, 'sec')

def ninth(file_name):
# abbreviations
	text = read_file(file_name)
	text = text.split('\n\n') 
	sentences = []
	for elt in text:
		# removing special characters with space
		elt = elt.replace('\n', ' ')
		elt = elt.replace('-', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('*', ' ')
		elt = elt .replace('#', ' ')
		elt = elt.replace('+', ' ')
		elt = elt.replace('^', ' ')
		elt = elt.replace('<', ' ')
		elt = elt.replace('>', ' ')
		elt = elt.replace('=', ' ')
		elt = elt.replace('|', ' ')
		elt = elt.strip()  # removing extra space at start and end
		initial = nltk.sent_tokenize(elt)   # tokenize to sentences
		for sub_elt in initial:
			sub_elt = re.sub(' +',' ',sub_elt)  # replace multiple spaces with a single space
			sentences.append(sub_elt)
	words = []
	tokenizer = RegexpTokenizer('\w+')  # '/w+' matches word characters equal to [a-zA-Z0-9_]
	for elt in sentences:
		filterdText = tokenizer.tokenize(elt)  # split sentences to words
		for sub_elt in filterdText:
			if not sub_elt.isnumeric():  # numeric word not added to list
				words.append(sub_elt)
	abbreviations = []
	for elt in words:
		count = 0
		for char in elt:
			if char.isupper():   # count of upper case characters is found in words
				count += 1
		if count >= 3:  # if count of upper case characters is more than 3 in a owrd it is considered an abbreviation
			abbreviations.append(elt)
	print('list of abbreviations:', abbreviations)

print('Enter name of file')
file_name = input()
while True:
	print('Enter task number')
	task = int(input())
	if task == 1:
		first(file_name)
	elif task == 2:
		second(file_name)
	elif task == 3:
		third(file_name)
	elif task == 4:
		print('Enter word to search')
		word = input()
		fourth(file_name, word)
	elif task == 5:
		print('Enter word to search')
		word = input()
		fifth(file_name, word)
	elif task == 6:
		print('Enter word to search')
		word = input()
		sixth(file_name, word)
	elif task == 7:
		seventh(file_name)
	elif task == 8:
		eighth(file_name)
	elif task == 9:
		ninth(file_name)
