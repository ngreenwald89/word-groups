"""
write a function to determine which category to assign user input
right now hand_tool and breakfast_food are the two options to choose from
domains can be extended by making a Domain() object and appending to
Inputs.domains list
To do:
"""

from word_similarity import get_best_synset_pair
from domain_class import Domain

class Inputs():

	def __init__(self, *args):
		self.inputs = list(args)
		self.assigned_domain = None
		self.domain = None
		self.domains = [Domain('hand_tool'), Domain('breakfast_food')]
		# self.default_domain = Domain('physical_entity') 'physical_entity has 39k hyponyms 
		# and takes along time to load, but thus might be a good default suggestion list'
		self.default_domain = Domain('food')
		self.assign_domain()

	def assign_domain(self):
		if self.inputs:
			highest = 0
			highest_domain = None
			for domain in self.domains:
				positive_matches = 0
				for inp in self.inputs:
					if inp in domain.word_list:
						positive_matches += 1
				if positive_matches > highest:
					highest = positive_matches
					highest_domain = domain
				elif positive_matches == highest and highest_domain:
					highest_domain = self.hypernym_best_match(
						highest_domain, domain, self.inputs)
			if highest_domain:
				self.assigned_domain = highest_domain
			else:
				self.assigned_domain = self.default_domain
		else:
			return "No inputs"

	def hypernym_best_match(self, domain1, domain2, inputs):
		count1 = 0
		count2 = 0
		for inp in inputs:
			count1 += get_best_synset_pair(domain1.root_word, inp)[1]
			count2 += get_best_synset_pair(domain1.root_word, inp)[1]
		if count1 >= count2:
			return domain1
		elif count2 > count1:
			return domain2

def example():
	# putting in the below words will get hypernym lists associated with categories
	# "hand_tool" and "breakfast_food", respectively
	hand_tool_example = Inputs('spade')
	breakfast_food_example = Inputs('cereal')
	# example of creating with multiple inputs
	multiple_inputs = Inputs('spade','cereal','apple')




