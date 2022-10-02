import nltk
from nltk.parse.generate import generate
from nltk import CFG
strG="""
S -> N V
N -> "Bakeel" | "Tawheed"
V -> "fast" | "go" """
grammer=CFG.fromstring(strG)
print(grammer)

for sent in generate(grammer):
	print(' '.join(sent))
