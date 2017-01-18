import re
import marisa_trie
import nltk
nltk.data.path.append('./nltk_data/')
from nltk.corpus import wordnet as wn

# http://stackoverflow.com/questions/26222484/determining-hypernym-or-hyponym-using-wordnet-nltk

# start with a category, like "tool", and get specific types like "hammer"
def hypodomain(domain):
	# make synset object for word's #1 noun meaning; #1 meaning not always what you expect
	domain = wn.synset('{}.n.01'.format(domain))
	# another way of getting synset object: domain = wn.synsets(domain, pos='n')[0]
	return set([i for i in domain.closure(lambda s:s.hyponyms())])


# clean synset string to the word itself: so 'car.n.01' becomes 'car'
find=re.compile(r"[\D]+?[?=.]")
def the_word(syn):
	return re.search(find, syn.name()).group(0)[:-1]

def word_list(hyponyms):
	hypolist = []
	for h in hyponyms:
		hypolist.append(the_word(h))
	return hypolist

def domainTrie(domain):
	hypoD = hypodomain(domain)
	DList = word_list(hypoD)
	return marisa_trie.Trie(DList)

if __name__ == '__main__':
	htTrie = domainTrie('hand_tool')
	foodTrie = domainTrie('food')
	bfTrie = domainTrie('breakfast_food')
	institutionTrie = domainTrie('institution')
