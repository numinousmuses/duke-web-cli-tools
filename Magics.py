#!/usr/bin/env python
# coding: utf-8

# 1. In the cell bellow, type and run `%lsmagic` to see all the available magic commands.
# 

# In[1]:


get_ipython().run_line_magic('lsmagic', '')


# 2. In the cell below type:
# 
# ~~~~
# %%sh
# 
# NAME=FRED
# echo $NAME
# ~~~~
# 
# This will run these shell commands and return the output.
# 

# In[2]:


get_ipython().run_cell_magic('sh', '', '\nNAME=FRED\necho $NAME')


# 3. Type and run `%history` in the cell below to see the inputs entered so far.

# In[3]:


get_ipython().run_line_magic('history', '')


# In[ ]:




