# word-groups
Word grouping problem

Given a group of words, and beginning letters, suggest words that 

1. start with the beginning letters and 

2. are similar to the group

Step 2 prototype in which_category.py, incorporates other files

Initial idea: use synsets, via WordNet

Domains so far: hand_tool, breakfast_food

Steps to run and load:

1. `$ git clone <repo>`

2. `$ virtualenv env` # to make environment, can `pip install virtualenv` if not installed

3. `$ source env/bin/activate`

4. `$ pip install -r requirements.txt`

5. `$ python3 -i which_category.py` #to see try out different word combinations and see what hyperdomain is chosen
