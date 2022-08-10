#!/usr/bin/env python
# coding: utf-8

# 1. In the cell below, type `1 + 3` and then hit Shift-Enter to run the cell and move to the next one.

# In[1]:


1 + 3


# 2. Type the following function definition and then run the cell:
# ```
# def add_one_mod_three(input_num):
#     return (input_num + 1) % 3
# ```

# In[2]:


def add_one_mod_three(input_num):
    return (input_num + 1) % 3


# 3. Call the function `add_one_mod_three` with 14 as an input and run it. Check the output below the cell.

# In[3]:


add_one_mod_three(14)


# 4. Type `dir_contents = !ls` to use the shell command `ls` to list the contents of the current directory, and capture them in the variable `dir_contents`

# In[4]:


dir_contents = get_ipython().getoutput('ls')


# 5. Print the variable `dir_contents`.

# In[5]:


print(dir_contents)


# In[ ]:




