#Import the lib perm from the package itertools in order to simplify the code
import random
from itertools import permutations
#---the comments bellow reffer to another implementation of the project that i tried and failed
#import numpy as np
#import ndarray for the array of the initial vector we need
#from numpy import ndarray
#==================================================
#1ST PART MAKE THE PERMUTATIONS
#input from keyboard
n = int(input('Enter an integer(it is the length of each permutation vector) :'))
#create an empty array with fixed size
#a = ndarray(n,int)
#init_array = np.array(n,np.int64);
#init vector input as a list
init_vec = list(range(1,n+1))
random.choice(init_vec)
print(init_vec)

#Get all permutations of the vector v = [n,n-1,n-2,.....,1]
#and length n
#the method permutations(initial vector, perm length) returns a list of vectors
perm = permutations(init_vec,n);
print("Permutation List is:")
for i in list(perm):
    print(i,sep = ",")

#--------------------------------------------------------------------------
#2ND PART make the smallest possible(length) vector with all permutation solutions and print it out
#easy way to only concatenate all the permutation
index = 0
output_vector = list()
for i in list(perm):
    output_vector.insert(index, i)
    index += 1
print("The concatenated list is:")
for x in range(len(output_vector)):
    print(output_vector[x])
#hard way to find the smallest vector with all the permutations