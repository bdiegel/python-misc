#! /usr/bin/python

##===========================================================================##
## computes skew of genome as difference between number of G's and C's 
## over substrings from length 0 to len( genome ) 
##===========================================================================##

from sys import exit

filename = 'data/find_oric_data.txt' #dataset_7_6.txt
ans = '80521 80652 80653 80671 80744 80745'

# Example data
input = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
ans = [ 11, 24 ]


# amount to adjust skew
deltas = { 'A': 0, 'T': 0, 'C': -1, 'G': 1 }


def main():        
   input = readData() 
   print ' '.join( str(x) for x in findMinSkew( input ) )
   

def skew( skew, c ):
   return skew + deltas[ c ]


def findMinSkew( seq ):
   curskew = 0; min = 0; locs = []
   
   for i in range( 0, len(seq)-1 ):
      head = seq[ i ]
      curskew = skew( curskew, head )
      if curskew <  min:
         min = curskew
         locs = [ i+1 ]
      elif curskew == min:
         locs.append( i+1 )
           
   return locs       


# sadly, Python does not support tail call optimization for recursion
# setrecursionlimit(75000) 
# def findMinSkew( seq, min, curskew, curloc, locs ):
#    if not seq:
#       return locs
#    
#    head, tail = seq[0], seq[1:]
#    
#    curskew = skew( curskew, head )
#    curloc += 1
#    
#    if curskew < min:
#       min = curskew
#       locs = [ curloc  ]
#    elif curskew == min:
#       locs.append( curloc ) 
#    
#    return findMinSkew( tail, min, curskew, curloc, locs )


def readData():
    f = open( filename, 'r' )
    return f.readline().strip()
   
        
# main 
if __name__ == "__main__":
    exit( main() )    
