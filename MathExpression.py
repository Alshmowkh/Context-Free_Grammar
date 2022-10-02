import nltk
from nltk import CFG
print("Start\n")
grmr=CFG.fromstring("""
S -> ID ':=' E
E -> N Er
Er -> '+' N Er
Er -> '-' N Er
Er -> ' '
""")
expression=input("Enter Math expression :")
#print("\n"+expression+"\n")
tokens=expression.split()
# for t in tokens:
#print(tokens[0])

def S():
    match(ID)
    match(':=')
    expr()
    return
def expr():
    match(N)
    exprR()
    return
def exprR():
    if (tok == '+'):
        match('+')
        match(N)
        exprR()
        return 0
    elif (tok == '-'):
        match('-')
        match(N)
        exprR()
        return
    else:
        match(' ')
def match(Token t):
    if (tok == t):
        tok=nextToken()
    else print("error")
    
#print(grmr)




