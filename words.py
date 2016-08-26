#This code counts the words from a .txt file and displays the word with most occurrences

name = raw_inpunt("Enter file:")
handle = open(name, "r")
text = handle.read()
words = text.split()
counts = dict()

for word in words:
	counts[word]=counts.get(word,0)+1
	
bigcount = None
bigword = None

for word, count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count
		
print bigword, bigcount
