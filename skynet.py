import re
import marisa_trie
import nltk
nltk.data.path.append('./nltk_data/')
from nltk.corpus import wordnet as wn

# http://stackoverflow.com/questions/26222484/determining-hypernym-or-hyponym-using-wordnet-nltk

class Domain():

	def __init__(self, root_word):
		self.root_word = root_word
		self.hypodomain = self.make_hypodomain(root_word)
		self.word_list = self.make_word_list(self.hypodomain)
		self.domainTrie = self.make_domain_trie(self.word_list)

	# start with a category, like "tool", and get specific types like "hammer"
	def make_hypodomain(self, word):
		# make synset object for word's #1 noun meaning; #1 meaning not always what you expect
		synset_obj = wn.synset('{}.n.01'.format(word))
		# another way of getting synset object: domain = wn.synsets(domain, pos='n')[0]
		return set([i for i in synset_obj.closure(lambda s:s.hyponyms())])


	# clean synset string to the word itself: so 'car.n.01' becomes 'car'
	find=re.compile(r"[\D]+?[?=.]")
	def cleaned_word(self, syn):
		return re.search(self.find, syn.name()).group(0)[:-1]

	def make_word_list(self, hyponyms):
		hypolist = []
		for h in hyponyms:
			hypolist.append(self.cleaned_word(h))
		return hypolist

	def make_domain_trie(self, word_list):
		return marisa_trie.Trie(word_list)

if __name__ == '__main__':
	hand_tools = Domain('hand_tool')
	food = Domain('food')
	breakfast_food = Domain('breakfast_food')
	institution = Domain('institution')


