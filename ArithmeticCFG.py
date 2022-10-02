
import nltk
from nltk import CFG
from nltk.parse.generate import generate
grmr=CFG.fromstring("""
    E -> E "+" E
    E -> E "-" E
    E -> E "*" E
    E -> "(" E ")"
    E -> "a"
    E -> "b"
    E -> "c"
""")
prs=generate(grmr)
x="hello"
    
