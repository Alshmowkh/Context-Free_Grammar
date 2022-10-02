import nltk
from nltk import CFG
from nltk.parse.generate import generate
grmr3=CFG.fromstring("""
E -> E '-' E
E -> 'a'
E -> 'b'
""")
