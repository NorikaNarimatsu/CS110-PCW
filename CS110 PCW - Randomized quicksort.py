#!/usr/bin/env python
# coding: utf-8

# Before you turn this problem in, make sure everything runs as expected. First, **restart the kernel** (in the menubar, select Kernel$\rightarrow$Restart) and then **run all cells** (in the menubar, select Cell$\rightarrow$Run All).
# 
# Note that this Pre-class Work is estimated to take **44 minutes**.
# 
# Make sure you fill in any place that says `YOUR CODE HERE` or "YOUR ANSWER HERE", as well as your name and collaborators below:

# In[10]:


NAME = "Norika Narimatsu "
COLLABORATORS = "Andriy"


# ---

# # CS110 Pre-class Work - Randomized quicksort
# 
# ## Part A. Median-of-3 partitioning quicksort 
# 
# ## Question 1 [time estimate: 10 minutes]
# 
# Read through the following Python code. What does each function (i.e., median, qsort, randomized_qsort, test_qsort) do? Comment in details each function. 
# 

# In[6]:


#  import necessarily libraly 
import timeit
import random

#  set value for calculation
eps = 1e-16
N = 10000
locations = [0.0, 0.5, 1.0 - eps]


def median(x1, x2, x3):
    '''
    this function calculates the middle value among 3 inputs
    Inputs:
    x1,x2,x3: the value will be compared
    output: x1 or x2 or x2 (middle value)
    
    Ex) median(1,2,3), output: 2
    '''
    if (x1 < x2 < x3) or (x3 < x2 < x1): #x2 is median
        return x2
    elif (x1 < x3 < x2) or (x2 < x3 < x1): #x3 is median
        return x3
    else: #x1 is median
        return x1

    
def qsort(lst):
    '''
    This function implements the quick sort in which the pivot is given by median()
    Input: list
    Output: Sorted list
    '''
    #  check the length of the list (# of iterations)
    indices = [(0, len(lst))]
    
    #  go through for loops as many times as the length of the lst
    while indices:
        (frm, to) = indices.pop()
        if frm == to:
            continue

        # Find the partition:
        N = to - frm
        inds = [frm + int(N * n) for n in locations]
        values = [lst[ind] for ind in inds]
        #. use median to make partition
        partition = median(*values)

        # Split into lists:
        # left side, which is smaller than median 
        lower = [a for a in lst[frm:to] if a < partition]
         # right side, which is bigger than median 
        upper = [a for a in lst[frm:to] if a > partition]
        counts = sum([1 for a in lst[frm:to] if a == partition])

        ind1 = frm + len(lower)
        ind2 = ind1 + counts

        # Push back into correct place:
        lst[frm:ind1] = lower
        lst[ind1:ind2] = [partition] * counts
        lst[ind2:to] = upper

        # Enqueue other locations
        indices.append((frm, ind1))
        indices.append((ind2, to))
    return lst


def randomized_quicksort():
    '''
    this function randomizes the input first, 
    and then use quick sort to output sorted array.
    '''
    
    lst = [i for i in range(N)]
    #shuffle the input of the quicksort
    random.shuffle(lst)
    # run quicksort and print out it
    return qsort(lst)

#test randomized quicksort
def test_quicksort():
    lst = randomized_quicksort()
    assert (lst == [i for i in range(N)])


# Is our algorithm correct
test_quicksort()

# How fast is our algorithm
print(timeit.timeit(randomized_quicksort, number=1))


# ## Question 2 [time estimate: 3 minutes]
# 
# What are the main differences between the `randomized_quicksort` in the code and $RANDOMIZED-QUICKSORT$ in Cormen et al., besides that the partition of `randomized_quicksort` uses a median of 3 as a pivot?

# Difference 1: The use of recursion. Cormen te al. uses recursion, PCW code use while loop
# 
# DIfference 2: the order of randomization. Cormen et al. shuffle before chosing pivot (pivot is random value selected from a list). PCW uses median as a pivot.
# 

# ## Question 3 [time estimate: 10 minutes]
# 
# What is the time complexity of this `randomized_qsort`? Time the algorithm on lists of various lengths, each list being a list of the first $n$ consecutive positive integers. Produce a graph with list lengths on the x axis and running time on the y axis. As always, don’t forget to time the algorithm several times for each list’s length and then average the results. 

# In[30]:


del list


# In[31]:


import time
import timeit
import matplotlib
import matplotlib.pyplot as plt 

## creating two lists - one for the list lengths, one for list times
list_times = []
list_lengths = list(range(1,1001))

for N in list_lengths:
    ## a list to calculate the average time for each input list
    average_list = []
    ## running the for loop for the same list length 10 times
    for i in range(1,11):
        a = timeit.timeit(randomized_quicksort, number=1)
        average_list.append(a)
    ## averaging it out
    b = sum(average_list)/len(average_list)
    ## appending to the list of times
    list_times.append(b)
    
plt.plot(list_lengths, list_times) 
plt.ylabel('Running time (in seconds)')
plt.title('Time Complexity graph of randomized_sort')
plt.show()


# ## Question 4.
# 
# ### Question 4a [time estimate: 7 minutes]
# 
# Change the `qsort()` function in a way that you **don’t** separate the items that are equal to the partition. In other word, you may want to put the partition in either ```lower``` or ```upper``` list instead of using ``counts`` and ```lst[ind1:ind2] = [partition] * counts``` as we did in question 1.

# In[32]:


def qsort_new(lst):

    indices = [(0, len(lst))]

    while indices:
        (frm, to) = indices.pop()
        if frm == to:
            continue

        # Find the partition:
        N = to - frm
        inds = [frm + int(N * n) for n in locations]
        values = [lst[ind] for ind in inds]
        partition = median(*values)

        # Split into lists:
        lower = [a for a in lst[frm:to] if a < partition]
        upper = [a for a in lst[frm:to] if a > partition]
        # deleted this line 
        #counts = sum([1 for a in lst[frm:to] if a == partition])

        ind1 = frm + len(lower)
        ind2 = ind1 + 1

        # Push back into correct place:
        lst[frm:ind1] = lower
        lst[ind1:ind2] = [partition]
        lst[ind2:to] = upper

        # Enqueue other locations
        indices.append((frm, ind1))
        indices.append((ind2, to))
    return lst

print(qsort_new([4,2,1])==[1,2,4])
print(qsort_new([0])==[0])


# In[40]:


assert(qsort([4,2,1])==[1,2,4])
assert(qsort([4,4,2,2,1,1])==[1,1,2,2,4,4])
assert(qsort([0])==[0])


# ### Question 4b [time estimate: 3 minutes]
# 
# Now time the algorithm on the same inputs you have used in question 3, adding one more line in the previous graph you have produced. 

# In[35]:


def randomized_quicksort_new():
    '''
    This randomized quicksort function randomizes the input (randomly shuffles it).
    It uses quicksort function after randomly shuffling the list.
    '''
    lst = [i for i in range(N)]
    random.shuffle(lst)
    return qsort_new(lst)

import time

## creating two lists - one for the list lengths, one for list times
list_times2 = []
list_lengths2 = list(range(1,1001))

for N in list_lengths2:
    ## a list to calculate the average time for each input list
    average_list2 = []
    ## running the for loop for the same list length 10 times
    for i in range(1,11):
        a = timeit.timeit(randomized_quicksort_new, number=1)
        average_list2.append(a)
    ## averaging it out
    b = sum(average_list2)/len(average_list2)
    ## appending to the list of times
    list_times2.append(b)
    

import matplotlib.pyplot as plt 

plt.plot(list_lengths2, list_times2, label = "Including separation") + plt.plot(list_lengths, list_times, label = "Excluding separation")  
plt.ylabel('Running time (in seconds)')
plt.title('Time Complexity graph of randomized_sort')
plt.legend()
plt.show()


# ## Question 5.
# 
# ### Question 5a [time estimate: 3 minutes]
# 
# Remove the median-of-3 partitioning, and just use the first element in the array. 

# In[14]:


def qsort_1st(lst):
    '''
    This function takes a list as an input at implements quicksort algorithm.
    It finds a partition, then compares left elements, and right elements, with a chosen pivot element.
    '''
    indices = [(0, len(lst))]

    while indices:
        (frm, to) = indices.pop()
        if frm == to:
            continue

        # Find the partition:
        partition = lst[frm]

        # Split into lists:
        lower = [a for a in lst[frm:to] if a < partition]
        upper = [a for a in lst[frm:to] if a > partition]
        counts = sum([1 for a in lst[frm:to] if a == partition])

        ind1 = frm + len(lower)
        ind2 = ind1 + counts

        # Push back into correct place:
        lst[frm:ind1] = lower
        lst[ind1:ind2] = [partition]*counts
        lst[ind2:to] = upper

        # Enqueue other locations
        indices.append((frm, ind1))
        indices.append((ind2, to))
    return lst

print(qsort_1st([4,2,1])==[1,2,4])
print(qsort_1st([0])==[0])


# In[43]:


assert(qsort([4,2,1])==[1,2,4])
assert(qsort([0])==[0])


# ### Question 5b [time estimate: 3 minutes]
# 
# Does this change the running time of your algorithm? Justify your response with a graph. 
# 
# 

# In[38]:


def randomized_quicksort_1st():
    '''
    This randomized quicksort function randomizes the input (randomly shuffles it).
    It uses quicksort function after randomly shuffling the list.
    '''
    lst = [i for i in range(N)]
    random.shuffle(lst)
    return qsort_1st(lst)

import time

## creating two lists - one for the list lengths, one for list times
list_times3 = []
list_lengths3 = list(range(1,1001))

for N in list_lengths3:
    # a list to calculate the average time for each input list
    average_list3 = []
    # running the for loop for the same list length 10 times
    for i in range(1,11):
        a = timeit.timeit(randomized_quicksort_1st, number=1)
        average_list3.append(a)
    # averaging it out
    b = sum(average_list3)/len(average_list3)
    # appending to the list of times
    list_times3.append(b)
    
import matplotlib.pyplot as plt 

plt.plot(list_lengths3, list_times3, label = "First element as a pivot") + plt.plot(list_lengths2, list_times2, label = "With separation") + plt.plot(list_lengths, list_times, label = "Without separation")  
plt.ylabel('Running time (in seconds)')
plt.title('Time Complexity graph of randomized_sort')
plt.legend()
plt.show()



#Using first element as a pivot shows slightly better running time, 
# however all three behaves simiar way with same notation (different coefficient).


# ## Part B. Recursive quicksort [time estimate: 5 minutes]
# 
# One main difference between the quicksort algorithms in Cormen et al. and the implementation in the code above is that quick sort (in the code in this notebook) is not recursive, while $QUICKSORT$ in Cormen et al. is. Given the limitation of Python so that it can only make 500 recursive calls, estimate the maximum size of the list that can be sorted by Python if a recursive quicksort is to be used. Explicitly state all assumptions you make in getting to an answer.
# 

# In the last class, we calculate the growth of dividion (quicksort) is 2^N. Depending on the input length, we will exceeds 500 recursive calls. 2^9 =512.
# 
