#! /usr/bin/python

##===========================================================================##
## finds occurrences of 'pattern' in 'sequence' and return locations 
##===========================================================================##

import itertools

from collections import deque
from sys import exit

filename = 'data/pattern_matching_data.txt'

def main():        
    ( s, p ) = readData()
    print occurs( s, p )

def occurs( seq, pattern ):
   queue = deque( seq )
   indices = []
   index = 0
   
   while ( len( queue ) >= len( pattern ) ):
      head = ''.join( list( itertools.islice( queue, 0, len( pattern ) ) ) )
      if head == pattern: indices.append( index )
      queue.popleft()
      index += 1
      
   return ' '.join( str(x) for x in indices )
    
def readData():
    f = open( filename, 'r' )
    pattern = f.readline().strip()
    seq = f.readline().strip()
    f.close()
    
    return (seq, pattern) 
    
# main 
if __name__ == "__main__":
    exit( main() )    
