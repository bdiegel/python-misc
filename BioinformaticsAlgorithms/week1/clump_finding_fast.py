#! /usr/bin/python

##===========================================================================##
## find distinct kmers forming clumps in E-coli
##===========================================================================##

from sys import exit

filename = 'data/E-coli.txt' 
k = 9
L = 500
t = 3
ans = 1904

def main():   
   seq  = readData()
   clumps = findClumps( seq, k, L, t )
   print "number of clumps: ", len( clumps )      


# finds kmers that occur at least 'clump_size' times within 'window_size' 
def findClumps( seq, k, window_size, clump_size ):
   kmerToLocs = findKmers( seq, k, clump_size )
   
   # look for clumps within the locations returned
   clumps = []
   for kmer in kmerToLocs.keys():
      locs = kmerToLocs[ kmer ] 
      if isClump( seq, locs, clump_size, window_size ):
         clumps.append( kmer)

   return ( clumps ) 


# determine if this kmer clumps together within the window 
def isClump( seq, locs, clump_size, window_size ):
   for index in range( 0, len(locs)-clump_size+1 ):
      if locs[ index + clump_size - 1] + k - locs[ index ] < window_size: 
         return True
   return False

   
# builds dictionary to map each kmer to list of locations in the dna sequence
def findKmers( seq, k, clump_size ):
   d = {}

   for index in range( 0, len(seq)-k ): 
      kmer = seq[ index : index+k ]
      if kmer not in d:
         d[ kmer ] = [ index ]
      else:
         d[ kmer ].append( index )

   return { k: v for k, v in d.iteritems() if len(v) >= clump_size }

    
def readData():
    f = open( filename, 'r' )
    seq = f.readline().strip()
    f.close()

    return seq
    
# main 
if __name__ == "__main__":
    exit( main() )    
