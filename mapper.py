import random
from optparse import OptionParser

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
map_fac = 2
change_prob = 50

def file_to_words(file):
    file.seek(0)
    data = file.read()
    return data.split("\n")

def segregate(words):
	dictio = {}
	for word in words:
		key = len(word)
		if key in dictio:
			dictio[key].append(word)
		else:
			dictio[key] = [word]
	return dictio
	
def getlen(word):
	word_len = len(word)
	if random.randint(1, 100) > change_prob:
		word_len += random.randint(0-map_fac, map_fac)
	if word_len < 2:
		word_len = 2
	return word_len
	
def map_words(words, dictio):
	cache = {}
	for word in words:
		word_len = getlen(word)
		#word_len = len(word)
		while len(dictio[word_len]) == 0:
			word_len = word_len + 1
		rand_choice = random.choice(dictio[word_len])
		dictio[word_len].remove(rand_choice)
		cache[word] = rand_choice
	return cache
	
def main():
	parser = OptionParser()
	parser.add_option('-e', '--eng-src', type='string', dest='s_eng', default='dictionary-sb-len.txt',
					  help='English dictionary')
	parser.add_option('-s', '--syn-src', type='string', dest='s_syn', default='dictiosyn-sb-len.txt',
					  help='Synthetic dictionary')
	parser.add_option('-m', '--map-fac', type='int', dest='map_fac', default=2,
					  help='Mapping Factor')
	parser.add_option('-c', '--change-prob', type='int', dest='change_prob', default=50,
					  help='Change Probability [1-100]: Probability of changing word length')
	(options, args) = parser.parse_args()
	
	map_fac = options.map_fac
	change_prob = options.change_prob
	
	f_eng = open(options.s_eng)
	f_syn = open(options.s_syn)

	eng_words = file_to_words(f_eng)
	syn_words = file_to_words(f_syn)
	
	eng_dictio = segregate(eng_words)
	syn_dictio = segregate(syn_words)
	
	#syn_dictio.__delitem__(2)
	#syn_dictio[2].remove('aa')
	#print(syn_dictio)
	mapping = map_words(eng_words, syn_dictio)
	#print(mapping)
	for key in mapping:
		print(key+" "+mapping[key])
	
if __name__ == '__main__':
	main()