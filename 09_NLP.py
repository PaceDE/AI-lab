import nltk 
# import all the resources for Natural Language Processing with Python 
nltk.download("book")  
sentence = """I just dont want to talk to 
you more after what happened.""" 
tokens = nltk.word_tokenize(sentence) 
print(tokens) 
tagged = nltk.pos_tag(tokens) 
print(tagged)