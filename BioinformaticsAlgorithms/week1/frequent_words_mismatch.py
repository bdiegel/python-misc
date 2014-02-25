#! /usr/bin/python

##===========================================================================##
## finds most 'frequent k-mers' with fewer than 'd' differences  
##===========================================================================##

from itertools import product
from sys import exit

filename = 'data/frequent_words_mismatch_data.txt'

acgt = set( ['A', 'C', 'G', 'T'] )

# Sample data
seq = 'ACGTTGCATGTCGCATGATGCATGAGAGCT' 
k = 4 
d = 1
ans = 'GATG ATGC ATGT'

# ACGTTGCATGTCGCATGATGCATGAGAGCT
# ---ATGC-------ATGC---ATGC-----  
# -------ATGC------ATGC---------
# --GATG-------GATG---GATG------
# ------GATG------GATG----------
# <more>


def main():        
   ( seq, k, d ) = readData() 
   freqKmers = freq_mismatches( seq, k, d )
   print ' '.join( x for x in freqKmers )

   
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
   
   # generate substrings of length k then generate and count 'mismatches' per substr   
   for substr in [ input[ i:i + k ] for i in range( 0, len( input ) - k + 1 )  ]:
      
      for kmer in mismatches( substr, d ):
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
