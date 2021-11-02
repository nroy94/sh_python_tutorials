#!/usr/bin/env python
# coding: utf-8

# # Lists
# 
# Python lists are similar to grocery lists in real life--they store items (usually called "elements") that can be different from eachother. Lists can store:
# 
#     - strings 
#     - integers
#     - other lists
#     - tuples
#     - dictionaries
#     - functions
#     - and more
# 
# They are very handy when you want to take a collections objects to do something with them (e.g. a list of dataframes and you want to transform the first column of each dataframe, go through the column names of a dataframe and standardize them all).
# 
# 
# **Table of Contents:**
# 
# a. <a href="#Indexing-a-List">Indexing a List</a><br>
# b. <a href="#List-Slicing">List Slicing</a><br>
# c. <a href="#Iterating-through-a-list">Iterating through a List</a><br>
# d. <a href="#List-Element-Assignment">List Element Assignment</a><br>
# e. <a href="#Tuples">Tuples</a><br>
# f.  <a href="#Zip-and-Enumerate">Zip and Enumerate</a><br>
# g. <a href="#Common-List-Methods">Common List Methods</a><br>
# h. <a href="#Sorting-Lists">Sorting Lists</a><br>
# h. <a href="#List-Comprehensions">List Comprehensions</a><br>

# List Syntax:
# 
# ### ```[item1, item2, item3, ...]```<br>
# 
# ### Indexing a List 
# 
# Python lists start with the 0 instead of 1.

# In[2]:


# let's use this sample list of string elements
# we store the list in the variable "friends"
friends = ['Chandler', 'Monica', 'Joey', 'Rachel', 'Ross', 'Kramer'] 


# <img src="list_indices_2.png" width = "1200" height="40">

# In[3]:


# we access the second element with 1, and so on
friends[0]


# In[24]:


# I take thee <>
friends[3]


# In[71]:


# notice that we have negative indices too

friends[-1]  # same as friends[0]


# ### List Slicing
# 
# What if we wanted to cut out a section of the list? That's what List Slicing is for!<br>
# 
# A good example of an application of list slicing is if you have data that's already randomized and you need to split it into training and test sets.
# 
# List splicing syntax is like so:<br>
# 
# ###  **```list[start:end:step]```**<br>
# 
# start and end will be indices.
# 
# Note that **<font color=orange>the end value is NOT included.</font>**<br>
# 
# [<a href="#Python-Common-Data-Structures">Back to top</a>]
#    
# <img src="list_indices_2.png" width = "1200" height="40">

# In[5]:


friends[1:5]  # get all friends besides the first and the last; remember the end is not included
friends[1:]  # get all friends besides the first; if we specify no end then every element after the start is included
friends[0:6] # gets all friends besides the last; equivalent to friend[0:5]
friends[2:-2] # worst couple and we just don't like friends in general...


# ### The Step
# 
# Consider the example below:

# In[84]:


friends[0:5] 
friends[0:5:1] # this is the same thing!


# This is what is happening, since the step is 1:
# 
# <img src="list_stepping_1.png" width = "900" height="20">
# 
# What if we increase the stepsize?

# In[7]:


friends[0:5:2] 


# <img src="list_stepping.png" width = "900" height="20">

# Now that we understand the syntax, let's look at some other examples with our list of friends.
# 
# <img src="list_indices_2.png" width = "900" height="20">
# 
# Syntax:
# 
# ###  **```list[start:end:step]```**<br>

# In[93]:


friends[1::2]  # what if we wanted to start with Monica and go every 2 and include Kramer?
friends[1:5:2]  # if you can't go the full step then that where the slice ends

# what if we wanted to go backwards?

# friends[4:0:-1] # start with Ross and then go until you hit Chandler. Notice start > end--the step's sign controls this.

# friends[0:4:-1] # something nonsensical returns an empty list

friends[-1:0:-1] # can use negative indices for the start and end as well; start at Kramer and go until Chandler


# ### Iterating through a list
# 
# We may traverse a list and use each element in the list to do something. We typically do this using a "for-loop."
# In a for-loop we go element-by-element in a list and then usually do something with each element
# <br><br>The syntax is:
# 
# ```python
# for i in list:
#     # do something with i
# ```

# In[9]:


# let's print out our list for visual aid
friends


# In[10]:


# i is a temporary variable that takes on the value of each element
# i changes its value to the next item in the list after everything in the body of the for-loop is done
for i in friends:
    print(i) # the body of the for-loop


# In[32]:


# the above is very similar to the folowing
i = 'Chandler'
print(i)
i = 'Monica'
print(i)
i = 'Joey'
print(i)
i = 'Rachel'
print(i)
i = 'Ross'
print(i)
i = 'Kramer'
print(i)
# etc.


# In[30]:


# we can change the "i" variable to be more clear
for friend in friends:
    print(friend + "!")


# There are many applications for using a for-loop and a list, but that's out of the scope for this tutorial. The main point here is to show the syntax.

# ### List Element Assignment
# 
# We may change the elements in a list.
# 
# syntax:
# 
# ### ```list[index] = <new value>```<br>
# 
# [<a href="#Lists">Back to top</a>]

# In[94]:


# let's print out the friends list again
friends


# In[98]:


# Let's change "Kramer" to "Phoebe"
friends[-1] = "Phoebe"
friends


# In[101]:


# multiple changes 
friends[:3] = ['Stanley', 'Phyllis', 'Dwight'] # new list doesn't have to be the same # of elements of the slice

friends


# In[15]:


# changing elements using steps
# the number of elements assigned DO matter
friends[1::2] = ['Angela', 'Kevin', 'Oscar']  # this will change Phyllis, Rachel, and Phoebe


# In[16]:


friends


# **<font color=gray>Extra Notes<font>**
# 
# <font color=gray>If you have select indices that need changes (no pattern) then there are other options as well like below:
# 
# ```python
# lst = [0,0,0,0,0]
# target = [99,98]
# pos = [2,5]
# for x,y in zip(pos,target):
#     lst[x] = y
# ```
#     
# Using numpy for this also works:
# 
# ```python
# import numpy as np
# lst = np.asarray([0,0,0,0,0])
# lst[[2,5]]=[99, 100]
# ```    
# <font color=gray>

# 
# ### Tuples
# 
# Tuples are an *another* data structure that are commonly used with lists and are similar to lists. Interestingly enough, they often appear _inside_ lists.
# 
# The tuple is a list that is "immutable" which means that it *cannot be changed* and therefore cannot be reordered.
# 
# Tuples, instead of brackets, use parenthesis, and each item is separated by commas. The syntax is below:
# 
# ### ```(item1, item2, item3)```<br>
# 
# [<a href="#Lists">Back to top</a>]
# 

# In[103]:


# a simple tuple
coordinates = (51, -.11, 5)


# In[104]:


# indexing
coordinates[0:2]


# In[39]:


# tuples inside of lists
country_coords = [('London', 51, -.11),
                  ('Alexandria', 31, 29.9),
                  ('Ankara', 39, 32.8)]


# In[105]:


# if we try to change it, we'll get an error.
coordinates = (51, -.11)
coordinates[0] = 1337


# ### Zip and Enumerate
# 
# Now that we know what lists and tuples are, we can use these two handy functions.
# 
# <br>
# [<a href="#Lists">Back to top</a>]

# ### Zip
# 
# Syntax:
# 
# ### ```zip(list1, list2, ...)```
# 
# 
# For example: 
# 
# If we have the lists ```['a', 'b', 'c']``` and ```[1, 2, 3]``` then ```zip(['a', 'b', 'c'], [1, 2, 3])``` would be:
# 
# ####  ```[('a', 1), ('b', 1), ('c', 3)]```

# In[107]:


# note that the zip() doesn't return a list, so we have to turn it into one. It's easier to print with this.
list(zip(['a', 'b', 'c'], [1, 2, 3]))


# In[21]:


# what if the lists are different sizes?
list(zip(['a', 'b'], [1, 2, 3])) 


# In[22]:


list(zip(['a', 'b', 'c'], [1, 2])) 


# In[23]:


list(zip(['a'], [1, 2, 3])) 


# This means that we can use a for-loop to traverse many lists at a time

# In[49]:


my_list = list(zip(['a', 'b', 'c'], [1, 2, 3]))
my_list


# In[109]:


for i, j in my_list:
    print(i + "!", j)


# In[26]:


# fun example
for i, j in my_list:
    print(i * j)


# <h3>Enumerate</h3>
# 
# Enumerate is very similar but you give it one list. Then, for each element in that list, it makes a tuple of that element and its index.
# 
# Syntax:
# 
# ### ```enumerate(list)``` 
# 
# 
# For example: 
# 
# ```enumerate(['Stress Relief', 'Dinner Party', 'Casino Night'])``` would make the object:

# ## ```[(0, 'Stress Relief'), (1, 'Dinner Party'), (2, 'Casino Night')]```

# In[27]:


list(enumerate(['Stress Relief', 'Dinner Party', 'Casino Night']))


# In[112]:


# we can set the start of the index too:
for index, episode in enumerate(['Stress Relief', 'Dinner Party', 'Casino Night'], start = 0):
    
    print(index, episode)


# ### Common List Methods
# 
# List objects have methods that let you further manipulate them.
# 
# Methods use dot syntax like so:<br>
# 
# ```python
# my_list.append(<new item>)
# ```
# 
# <font color=gray>Note that some of these don't work on tuples<font>
# 
# [<a href="#Lists">Back to top</a>]
# 
# <img src="list_functions.png" width = "1200" height="40">

# In[115]:


fave_food = []

# let's add our favorite places to eat in Grand Rapids
fave_food.append('ming ten')
fave_food.append("taco's al cunado")
fave_food.append("cousin's tasty chicken")


# In[116]:


fave_food


# In[120]:


fave_food.reverse()
fave_food


# In[121]:


fave_fast_foods = ["mcdonad's", "taco bell", "wendy's"]


# In[122]:


fave_food.extend(fave_fast_foods)  # we can also do this with the + operator


# In[123]:


fave_food


# In[57]:


# delete the movies you don't like using pop and remove

movies = [
    "Batman vs. Superman Dawn of Justice",
    "Marvel Avenger Movies",
    "Napolean Dynamite",
    "Avatar",
    "any new Stars Wars movie",
    "Frozen",
    "Titanic",
    "Star Wars prequels",
    "Despicable Me 2",
    "Toy Story 4",
    "The Fate of the Furious",
    "Kazaam",
    "Space jam 2",
]


# In[124]:


# from the above pop or delete the one you hate!
movies.pop(2)


# In[125]:


movies


# ### Sorting Lists
# 
# We can sort a list either ascending or descending. We can also choose _what_ part of the element to sort by.
# 
# Syntax:
# 
# ### ```list.sort(key = <function>, reverse = <boolean>)```
# <br>
# Sorting only works if the elements can be compared (e.g. we can't sort a list of both integers and strings).
# 
# [<a href="#Lists">Back to top</a>]
# 
# 

# In[127]:


my_list = ['a','c', 'b']

# typically if you exclude the arguments, then it'll sort ascending
my_list.sort(reverse = True)

my_list


# In[38]:


# we may sort descending
my_list.sort(reverse = True)
my_list


# In[128]:


# what if we have elements that are list-like?

my_list = [('a', 1),  ('c', 2), ('b', 3)]


# In[131]:


my_list.sort() # this naturally sorts by the first element of each tuple element
my_list
# we can sort by the second item in the list as well
my_list.sort(key = lambda item: item[1])
my_list


# ### List Comprehensions
# 
# A shorthand way to write lists based on other lists.
# 
# Syntax:
# 
# ### ```[item for item in list]```
# <br>
# 
# [<a href="#Lists">Back to top</a>]
# 
# 

# In[132]:


# Let's say that we what to take a list of numbers and square them

my_numbers = [1, 2, 3, 4]

my_squares = [] 
for number in my_numbers:
    my_squares.append(number ** 2)


# In[133]:


my_squares


# In[43]:


# list comprehension version; this compresses the 3 lines of code into one
[number ** 2 for number in my_numbers]


# List comprehensions work with conditions too:
# 
# ### ```[item for item in list if (condition)]```<br>

# In[134]:


my_numbers = [1, 2, 3, 4]

my_even_squares = [] 
for number in my_numbers:
    if number % 2 == 0:
        my_even_squares.append(number ** 2)


# In[135]:


my_even_squares


# In[136]:


# equivalent; compress 4 lines of code
[number ** 2 for number in my_numbers if number % 2 == 0]


# #### Practical Example with Pandas DataFrame

# In[137]:


import pandas as pd

df = pd.DataFrame({'Names': ['James', 'Peter', 'Matthew'],
                  'Age Group':['Adult', 'Senior', 'Child'],
                  'country name': ['Canada', 'Germany', 'Turkey']})


# In[138]:


df


# In[139]:


# standardize the name with a list comprehension

df.columns = [col_name.lower() for col_name in df.columns]


# In[140]:


df

