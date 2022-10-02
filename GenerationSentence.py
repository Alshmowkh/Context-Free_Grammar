import nltk
from nltk import CFG
from nltk.parse.generate import generate

grmr2=CFG.fromstring("""
 S -> NP VP
    NP -> Det N
    PP -> P NP
    VP -> 'slept'
    VP -> 'saw' NP
    VP -> 'walked' PP
    Det -> 'the'
    Det -> 'a'
    N -> 'man'
    N -> 'park'
    N -> 'dog'
    P -> 'in'
    P -> 'with'
""")
prs2=generate(grmr2)

