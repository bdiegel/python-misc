#! /usr/bin/python

##===========================================================================##
## finds approximate matches of 'p' in 'seq' with fewer than 'd' differences  
##===========================================================================##

from sys import exit

filename = 'data/approximate_match_data.txt'

# Sample data
# seq = "ACATGACACAAACATATGGGTGCAGTAGCTTGGAACAGTAGCT"
# p = "CATGA"
# d = 2


def main():        
    (seq, p, d ) = readData()
    print ' '.join( str(x) for x in approx_match( seq, p, d ) )


def approx_match( seq, pattern, d ):
   locs = []
   
   for (str, i) in [ ( seq[ i: i + len( pattern ) ], i ) for i in range( 0, len( seq ) - len( pattern ) + 1 ) ]:
      diffs = sum ( str[ i ] != pattern[ i ] for i in range( len( pattern ) ) )
      if diffs <= d:
         locs.append( i )
         #print 'str: {0} at i: {1}'.format( str, i )
         
   return locs
    
def readData():
    f = open( filename, 'r' )
    pattern = f.readline().strip()
    seq = f.readline().strip()
    d = f.readline().strip()
    f.close()
    
    return ( seq, pattern, int( d ) ) 
    
# main 
if __name__ == "__main__":
    exit( main() )    
