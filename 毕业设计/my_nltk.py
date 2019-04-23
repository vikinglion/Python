#!usr/bin/env python
import nltk

#nltk.download('wordnet')
text = "this is XIAOHAI's text, isn't it?"
tokenizer = nltk.tokenize.WhitespaceTokenizer()

print(tokenizer.tokenize(text))

tokenizer = nltk.tokenize.WordPunctTokenizer()

print(tokenizer.tokenize(text))
