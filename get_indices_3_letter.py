def word_reader(filename):
  # returns an iterator
  return [word.strip() for word in open(filename)]

word_dict = word_reader("./dict_new")


id_dict = {}

s = 'abcdefghijklmnopqrstuvwxyz'

for i in s:
	for j in s:
		for k in s:
			id_dict[i+j+k] = 0

print(id_dict)


for letter in id_dict:
	for i, word in enumerate(word_dict):
		if word.startswith(letter):
			id_dict[letter] = i
			print(word)
			break
	else:
		id_dict[letter] = -1

print(id_dict)
key = [i for i in id_dict]
value = [id_dict[i] for i in id_dict]


with open('key2.txt', 'w') as filehandle:
    for listitem in key:
        filehandle.write('%s\n' % (listitem))

with open('value2.txt', 'w') as filehandle:
    for listitem in value:
        filehandle.write('%s\n' % (listitem))