#! /usr/bin/python

##===========================================================================##
## computes skew of genome as difference between number of G's and C's 
## over substrings from length 0 to len( genome ) 
##
## note: simple but not efficient for large strings
##===========================================================================##

from operator import itemgetter
from sys import exit

filename = 'data/find_oric_data.txt'

# Example data
input = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
ans = [ 11, 24 ]


def main():        
   input = readData()
   skews = skew( input )
   print ' '.join( str(x) for x in findMin( skews ) )


def findMin( skews ):
   return [ i for (i, v) in enumerate( skews ) if v == min( skews ) ]


def skew( seq ):
   skews = []
   for p in [ seq[ 0: i ] for i in range( 0, len(seq)+1 ) ]:
      skews.append( str( p.count( 'G' ) - p.count( 'C' ) ) )
   return skews


def readData():
    f = open( filename, 'r' )
    return f.readline().strip()
   
        
# main 
if __name__ == "__main__":
    exit( main() )    
