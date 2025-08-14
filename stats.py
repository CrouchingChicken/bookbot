def get_num_words(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		num_words = file_contents
	y = num_words.split()
	x = len(y)
	#return print(f"{x} words found in the document")
	return x

def sort_on(item):
	return item["num"]

def number_of_chars(filepath):
	chars = {} # empty dictionary
	dictable = []
	with open(filepath) as f:
		file_contents = f.read()
		num_words = file_contents
	for words in num_words:
		lowered = words.lower()
		if lowered in chars:
			chars[lowered] += 1
		else:
			chars[lowered] = 1
	
	for keys, num in chars.items():
		dictable.append({'char': keys, 'num': num})

	
	dictable.sort(reverse=True, key=sort_on)
	for keys in dictable:
		if keys['char'].isalpha():
			print(f"{keys['char']}: {keys['num']}")
	return dictable	

