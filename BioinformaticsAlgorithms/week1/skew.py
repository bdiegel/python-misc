#! /usr/bin/python

##===========================================================================##
## computes skew of genome as difference between number of G's and C's 
## over substrings from length 0 to len( genome ) 
##===========================================================================##

from sys import exit

# Example data
#input = "CATGGGCATCGGCCATACGCC"
input = "GAGCCACCGCGATA"

def main():        
   print " ".join( skew( input ) ) 

def skew( seq ):
   skews = []
   for p in [ seq[ 0: i ] for i in range( 0, len(seq)+1 ) ]:
      skews.append( str( p.count( 'G' ) - p.count( 'C' ) ) )
   return skews
   
        
# main 
if __name__ == "__main__":
    exit( main() )    
