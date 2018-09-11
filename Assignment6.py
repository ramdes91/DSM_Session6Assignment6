
# coding: utf-8

# In[35]:


import numpy as np
x = np.array([1, 2, 3,4,5,6])
np.vander(x)
np.vander(x, increasing=False)
print(np.vander(x, increasing=False))




