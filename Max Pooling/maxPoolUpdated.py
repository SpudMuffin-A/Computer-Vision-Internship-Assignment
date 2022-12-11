from collections import deque
import numpy as np
def maxPool(arr, n, k):
  '''Updated Max pooling on 2D data.

    <arr>: ndarray, input array to pool.
    <n>: integer, size of the matrix.
    <k>: tuple of 2, kernel size in (ky, kx).

    Return <result>: pooled matrix.
    '''
  
    dq = deque() # Define the doubly ended queue, that will behave like a monotonic doubly ended queue.
    res = []

    for i in range (k):
        while(dq and
            arr[dq[-1]] <= arr[i]):
            dq.pop()
        dq.append(i)
    

    for i in range (k, n):
        res.append(arr[dq[0]]) #Print the element at the head of the queue.

        while(dq and dq[0] <= i - k):
            dq.popleft() #Remove the elements which no longer lies in the window.

        while(dq and arr[dq[-1]] <= arr[i]):
            dq.pop() #Pop out all elements from the tail that are smaller than a[i].
            
        dq.append(i)
    
    res.append(arr[dq[0]]) #Print the element at head of the queue that is maximum element of last window.
    return res

  
arr = np.array([[  20,  200,   -5,   23],
       [ -13,  134,  119,  100],
       [ 120,   32,   49,   25],
       [-120,   12,   9,   23]]) #Input Array

r =[]
for x in arr:
    r.append(maxPool(x, len(x), 2))     #Calculate the sliding window maximum for each row

col = list(zip(*r)) #Storing the column of previous rows in a list
fin = []
for x in col:
    fin.append(maxPool(x, len(x), 2))  #Calculate the sliding window maximum for each column

y = np.array(fin) #Transposing the final answer
ans = np.transpose(y)
print(ans)
