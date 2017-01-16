from pprint import pprint
import itertools
import nltk
nltk.data.path.append('./nltk_data/')
from nltk.corpus import wordnet as wn

# from this site, with some modifications
# switched in wup for path_similarity
# http://sujitpal.blogspot.in/2014/12/semantic-similarity-for-short-sentences.html
######################### word similarity ##########################

def get_best_synset_pair(word_1, word_2):
    comps = 0
    """ 
    Choose the pair with highest path similarity among all pairs. 
    Mimics pattern-seeking behavior of humans.
    """
    max_sim = -1.0
    # since we're doing items, only care about nouns. verb to noun comp may return None
    synsets_1 = wn.synsets(word_1, pos='n')
    synsets_2 = wn.synsets(word_2, pos='n')
    if len(synsets_1) == 0 or len(synsets_2) == 0:
        return None, None
    else:
        max_sim = -1.0
        best_pair = None, None
        for synset_1 in synsets_1:
            for synset_2 in synsets_2:
               comps +=1
               # sim = wn.path_similarity(synset_1, synset_2)
               sim = wn.wup_similarity(synset_1, synset_2)
               if sim > max_sim:
                   max_sim = sim
                   best_pair = synset_1, synset_2
        print('comps', comps)
        return (best_pair, max_sim)


def compare_list(my_list):
  best_pairs = []
  for a, b in itertools.combinations(my_list, 2):
      best_pair = get_best_synset_pair(a, b)
      best_pairs.append(best_pair)
  return best_pairs


if __name__ == '__main__':
  tools = [
  'knife', 'rod', 'shovel', 
  'fan', 'belt', 'pick', 'axe', 
  'sandpaper', 'glue', 'wood', 'wrench', 
  'screwdriver', 'brush'
  ]
  bp = compare_list(tools)
  pprint(bp)
