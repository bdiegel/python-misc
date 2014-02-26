voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    d = dict()
    for senator_data in voting_data:
       rec = senator_data.split()
       votes = rec[3 : len(rec) ]
       d[ rec[0] ] =  [ int(i) for i in votes ]
    return d
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    arec = voting_dict[ sen_a ]
    brec = voting_dict[ sen_b ]
    dotprod = sum( [ x * y for (x, y) in zip( arec, brec ) ] )
    
    return dotprod


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    rec = voting_dict[ sen ]

    senators = list( voting_dict.keys() )
    senators.remove( sen )
    most_similar = senators[ 0 ] 
    min = -1 * (len( rec ) + 1)

    for next_senator in senators:       
       dotprod = policy_compare( sen, next_senator, voting_dict )
       if dotprod > min:
         min = dotprod
         most_similar = next_senator
    return most_similar

    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    rec = voting_dict[ sen ]

    senators = list( voting_dict.keys() )
    senators.remove( sen )
    least_similar = senators[ 0 ] 
    max = 1 * ( len( rec ) + 1 )

    for next_senator in senators:       
       dotprod = policy_compare( sen, next_senator, voting_dict )
       if dotprod < max :
         max = dotprod
         least_similar = next_senator
    return least_similar
    
    

## Task 5

most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold' 



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    cs = list()
    for sen_next in sen_set:
      cs.append( policy_compare( sen, sen_next, voting_dict) )
    print( cs )
    print( 'sum: ' + str(sum(cs)) )
    print( 'len: ' + str(len(cs)) )
    return sum( cs )/ len(cs)

def getDems(vd):
   dems = list()
   for data in vd:
      rec = data.split()
      if rec[1] == 'D':
         dems.append( rec[0] )
   return dems

'''
def find avgDem():
   for d in ds:
      a = politics_lab.find_average_similarity( d, ds, vd)
      print( d + ' = ' + str(a) )
'''

democrats = getDems( voting_data )
most_average_Democrat = 'Biden' # give the last name (or code that computes the last name)

# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    sums = [0] * len(voting_dict[ sen_set[0] ])
    for sen in sen_set:
       rec = voting_dict[ sen ]
       sums = [ rec[i] + sums[i] for i in range(len(rec)) ]
    
    print( 'sums: ' + str(sums) )
    print( 'len: ' + str(len(sen_set)) )
    return [ sums[i]/len(sen_set) for i in range(len(sums)) ]


voting_dict = create_voting_dict() 
average_Democrat_record = find_average_record( democrats, voting_dict ) 

# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    senators = voting_dict.keys()
    rivals = ( '', '' )
    min = 100
    for sen in senators: 
       sen_b = least_similar( sen, voting_dict )
       c =  policy_compare( sen, sen_b, voting_dict )
       if c < min:
          rivals = ( sen, sen_b)
          min = c

    return rivals

