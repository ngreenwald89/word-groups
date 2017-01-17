import re
import nltk
nltk.data.path.append('./nltk_data/')
from nltk.corpus import wordnet as wn
import marisa_trie

# http://stackoverflow.com/questions/26222484/determining-hypernym-or-hyponym-using-wordnet-nltk

def hypodomain(domain):
	domain = wn.synsets(domain, pos='n')[0]
	return set([i for i in domain.closure(lambda s:s.hyponyms())])

def first_n(word): 
	return wn.synset('{}.n.01'.format(word))


find=re.compile(r"[\D]+?[?=.]")

def the_word(syn):
	return re.search(find, syn.name()).group(0)[:-1]

def word_list(hyponyms):
	hypolist = []
	for h in hyponyms:
		hypolist.append(the_word(h))
	return hypolist

if __name__ == '__main__':
	hypotools = hypodomain('tool')
	tools = word_list(hypotools)
	toolTrie = marisa_trie.Trie(tools)
