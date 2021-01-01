
import nltk
import re
from nltk.tree import Tree



def driver():
    myTree = Tree(1, [2, Tree(3, [4]), 5])
    print (myTree);

def driver2():
    vp = Tree('VP', [Tree('V', ['saw']),Tree('NP',['him'])])
    s = Tree('S', [Tree('NP', ['I']), vp])
    print (s);
    print (s[1]);
    print (s[1,1]);

def driver3():
    np = Tree('NP',[Tree('DT',['The']),Tree('NN',['people'])])
    vp = Tree('VP',[Tree('V', ['saw']),Tree('NP',['him'])])
    s = Tree('S', [Tree(np,vp)])
    print (s);

'''
In the analysis of this tree structure, the statement
"I saw him" is broken up into a "VP" verb phrase on the first line
and a sentence "s" on the second line that contains a Sentence "S"
with a NP noun phrase "I" and the verb phrase on the first line.

This means "S" contains two elements NP and VP; the VP contains two
elements a V (saw) and a NP (him).  
'''
def driver4():
    vp = Tree('VP', [Tree('V', ['saw']),Tree('NP',['him'])])
    s = Tree('S', [Tree('NP', ['I']), vp])
    print (s);
    print (s[0]);
    print (s[1,0]);
    print (s[1,1]);

def driver5():
    vp = Tree('VP', [Tree('V', ['saw']),Tree('NP',['him'])])
    s = Tree('S', [Tree('NP', ['I']), vp])
    print (s.label());
    print (s[0].label());
    print (s[1,0].label());
    print (s[1,1].label());

def driver7():
    text = "A covered entity may use or disclose protected health information, provided that the individual is informed in advance of the use or disclosure and has the opportunity to agree to or prohibit or restrict the use or disclosure, in accordance with the applicable requirements of this section. The covered entity may orally inform the individual of and obtain the individual's oral agreement or objection to a use or disclosure permitted by this section."
    print ();
 

def main():
    driver7();

if __name__ == "__main__": 
    # calling main function 
    main()













    
