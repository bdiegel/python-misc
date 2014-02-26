# Please fill out this stencil and submit using the provided submission script.





## Problem 1
#def myFilter(L, num): pass
def myFilter(L, num): 
    return [ x for x in L if x % num != 0 ]


## Problem 2
#def myLists(L): pass
def myLists(L): 
    return [ list( range(1, x+1) ) for x in L ]

## Problem 3
#def myFunctionComposition(f, g): pass
def myFunctionComposition(f, g): 
    return { i:g[f[i]] for i in f }

## Problem 4
# Please only enter your numerical solution.

complex_addition_a = (5+3j) 
complex_addition_b = 1j
complex_addition_c = (-1+0.001j)
complex_addition_d = (0.001+9j)



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
#def mySum(L): pass
def mySum(L): 
    current = 0
    for i in L:
       current = current + i
    return current


## Problem 7
#def myProduct(L): pass
def myProduct(L):
    current = 1;
    for i in L:
       current = current * i
    return current


## Problem 8
#def myMin(L): pass
def myMin(L):
    current = L[0]
    for i in L:
       current = ( i if i < current else current )
    return current



## Problem 9
#def myConcat(L): pass
def myConcat(L):
    cur = ''
    for s in L:
       cur = cur + s
    return cur



## Problem 10
#def myUnion(L): pass
def myUnion(L):
    current = set()
    for s in L:
       current = current | s
    return current

