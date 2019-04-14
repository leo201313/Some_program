#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import time
start = time.time()
M = np.genfromtxt('ranmat.txt',dtype=int,delimiter=' ')
n = M.shape[0]
# n=4
# M=np.zeros((n,n),int)
# M[0,1] = 1
# M[1,3] = 1
# M[3,0] = 1
# M[3,2] = 1
print('The matrix read is like:\n')
print(M)
A = np.copy(M)



# In[2]:


for col in range(n):
    print(col)
    st_row = np.expand_dims(A[col,:],axis=0)
    bool_col_1 = A[:,col] == 1
    num_1 = A[bool_col_1,:].shape[0]
    if num_1 == 0:
        continue
    elif num_1 == 1:
        A[bool_col_1,:] = st_row | A[bool_col_1,:]
    else:
        to_change = st_row
        for ele in range(num_1-1):
            to_change = np.concatenate((to_change,st_row),axis=0)
        A[bool_col_1,:] = to_change | A[bool_col_1,:]
end = time.time()        
print('The t(R) is like:\n')
print(A)
print('\nThe total time is:')
print(end-start)

            
        
#     print(bool_col_1)
#     print(A[bool_col_1,:])
#     print(A[bool_col_1,:].shape)
#     A[bool_col_1,:] = A[bool_col_1,:] |  


# In[ ]:




