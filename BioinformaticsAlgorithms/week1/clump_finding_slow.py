#! /usr/bin/python

##===========================================================================##
## find distinct kmers forming clumps
##===========================================================================##

import itertools

from collections import Counter, deque
from sys import exit

filename = 'data/clump_finding_data.txt'


def main():   
    ( seq, args ) = readData()    
    print clumps( seq, int(args[0]), int(args[1]), int(args[2]) )


def clumps( seq, k, L, t ):
   queue = deque( seq )
   kmers = []
   index = 0
   
   while ( len( queue ) >= L ):
      head = ''.join( list( itertools.islice( queue, 0, L ) ) )
      hits = freqKmers( seq, k, t)
      kmers.extend( hits )      
      queue.popleft()
      index += 1
      
   return ' '.join( sorted(set(kmers)) )
    

def freqKmers( seq, k, t ):
    d = Counter( [ seq[ i:i+k ] for i in range( 0, len( seq )-k+1 ) ] )
    return filter( lambda x: d[x] >= t, d )

    
def readData():
    f = open( filename, 'r' )
    seq = f.readline().strip()
    args = f.readline().strip().split( ' ')
    f.close()
    
    return ( seq, args )
    
# main 
if __name__ == "__main__":
    exit( main() )    
