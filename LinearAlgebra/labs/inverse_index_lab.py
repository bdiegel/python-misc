from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[ randint(0,2) ]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    #return ...
    #e = enumerate( strlist.split() )
    #return { w : {i} for ( i, w ) in e }

    # [['the', 'quick', 'fox'], ['the', 'fox', 'and', 'the', 'hound']]
    lstrs = [ str.split() for str in strlist ]

    # [(0, ['the', 'quick', 'fox']), (1, ['the', 'fox', 'and', 'the', 'hound'])]
    elstrs = enumerate(lstrs)

    #[(0, 'the'), (0, 'quick'), (0, 'fox'), (1, 'the'), (1, 'fox'), (1, 'and'), (1, 'the'), (1, 'hound')]
    indices = [ ( n, w) for (n, ws) in elstrs for w in ws ]
  

    d = dict()
    for ( i, w ) in indices:
        s = set([i])
        if w in d :
            d[w] = d[w] | s 
        else:
            d[w] = s

    return d

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    #return ( s.add( inverseIndex[w])  for w in query )

    s = set()
    for w in query:
        s = s | inverseIndex[w]
    return s

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    # return ... 

    s = inverseIndex[ query[0] ] 
    for w in query:
        s = s & inverseIndex[w]
    return s
