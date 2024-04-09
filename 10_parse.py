import nltk 
from nltk.tree import Tree 
# Example sentence and parse tree string 
sentence = "The dog is chasing the cat." 
parse_tree_string = "(S (NP (Det The) (N dog)) (VP (V is) (NP (V chasing) (Det the) (N cat))))" 
# Convert the parse tree string into an NLTK Tree object 
parse_tree = Tree.fromstring(parse_tree_string) 
# Draw the parse tree 
parse_tree.pretty_print()