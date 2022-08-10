#!/usr/bin/env python
# coding: utf-8

# 1. In the cell below, type `my_var = "HiYa"`, then run the cell by using the run button above, or by typing Shift-Enter

# In[1]:


my_var="HiYa"


# 2. In the cell below, type `print(my_var)`. Then run the cell to confirm that the value set in the previous cell is sustained in subsequent cells.

# In[2]:


print(my_var)


# 3. In the cell below, type `import os` and run the cell, to import the os module.

# In[3]:


import os


# 4. In the cell below, type `os.` and then tab to see attributes available on the os module.
# 5. Do this agian, then start typing "lis" to filter the options to the listdir function.

# In[4]:


os.listdir


# 6. Type `os.listdir?` to see the function documention.

# In[5]:


get_ipython().run_line_magic('pinfo', 'os.listdir')


# 7. Type `!pwd` to run the shell command `pwd` from within this notebook.

# In[6]:


get_ipython().system('pwd')


# In[ ]:




