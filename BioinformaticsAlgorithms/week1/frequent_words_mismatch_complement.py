#! /usr/bin/python

##===========================================================================##
## most frequent k-mers (with mismatches and reverse complements) in 'seq'  
##===========================================================================##

from itertools import product
from string import maketrans
from sys import exit

filename = 'data/frequent_words_mismatch_data.txt'
filename = 'data/dataset_8_5.txt'

acgt = set( ['A', 'C', 'G', 'T'] )

# Sample data
seq = 'ACGTTGCATGTCGCATGATGCATGAGAGCT' 
k = 4 
d = 1
ans = 'ATGT ACAT'

# ACGTTGCATGTCGCATGATGCATGAGAGCT
# ATGT---ATGT---ATGT---ATGT-----
# -----------------ATGT---------
# ACAT-ACAT---ACAT---ACAT-------



def main():        
   ( seq, k, d ) = readData() 
   freqKmers = freq_mismatches( seq, k, d )
   print ' '.join( x for x in freqKmers )


def reverseComplement( seq ):
    return seq.translate( maketrans( "ACGT", "TGCA" ) ) [::-1]   
   
   
# generate single mutations of kmer
def single_mutations( kmer ):
   mismatches = []
   for i in range( 0, len( kmer ) ) :
      c = kmer[ i ]      
      pre = kmer[ 0: i]
      post = kmer[ i+1: len( kmer ) ]
      diffs = acgt - set( [ c ])
      
      for d in diffs:
         mismatches.append( pre + d + post )
         
   return mismatches

# recursively generate mismatches to depth d
def mismatches( kmer, d ):
   
   if d == 0: return []
   
   single_mutations_kmer = single_mutations( kmer )
   all_mutations = set( single_mutations_kmer )
   all_mutations.update( [ kmer ] )
   
   for mutation in single_mutations_kmer:
      all_mutations.update( mismatches( mutation, d-1 ) )   
       
   return all_mutations


def freq_mismatches( input, k, d ):
   freqs = {}
   
   # generate substrings of length k then generate    
   for substr in [ input[ i:i + k ] for i in range( 0, len( input ) - k + 1 )  ]:
      
      # count 'mismatches' per substr
      for kmer in mismatches( substr, d ):
         if kmer not in freqs:
               freqs[ kmer ] = 1
         else:
               freqs[ kmer ] = freqs[ kmer ] + 1
               
      # count 'mismatches' for reverse complement of substr
      substr_rc = reverseComplement( substr )
      for kmer in mismatches( substr_rc, d ):
         if kmer not in freqs:
               freqs[ kmer ] = 1
         else:
               freqs[ kmer ] = freqs[ kmer ] + 1
      
               
   m = max( freqs.values() )
   return [ k for k, v in freqs.items() if v == m ]

    
def readData():
    f = open( filename, 'r' )
    seq = f.readline().strip()
    (k, d) = f.readline().strip().split( ' ' )
    f.close()
    
    return ( seq, int(k), int( d ) ) 
    
# main 
if __name__ == "__main__":
    exit( main() )    
