import nltk
nltk.data.path.append('./nltk_data/')
from nltk.corpus import wordnet as wn

# http://stackoverflow.com/questions/26222484/determining-hypernym-or-hyponym-using-wordnet-nltk

def hypodomain(domain):
	domain = wn.synsets(domain, pos='n')[0]
	return set([i for i in domain.closure(lambda s:s.hyponyms())])

if __name__ == '__main__':
	hypotools = hypodomain('tool')