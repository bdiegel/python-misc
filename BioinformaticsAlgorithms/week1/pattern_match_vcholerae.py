#! /usr/bin/python

##===========================================================================##
## finds occurrences of 'pattern' in 'sequence' and return locations 
##===========================================================================##

import itertools

from collections import deque
from sys import exit

filename = 'data/Vibrio_cholerae.txt'
pattern = 'CTTGATCAT'
#pattern = 'ATGATCAAG'

def main():        
    seq = readData()
    print occurs( seq, pattern )

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
    seq = f.readline().strip()
    f.close()
    
    return seq
    
# main 
if __name__ == "__main__":
    exit( main() )    
