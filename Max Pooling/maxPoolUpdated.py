from collections import deque
import numpy as np
# Function to print maximum element of
# each window of size k.
def maxPool(arr, n, k):
  '''Non-overlapping pooling on 2D or 3D data.

    <arr>: ndarray, input array to pool.
    <n>: integer, size of the matrix.
    <k>: tuple of 2, kernel size in (ky, kx).

    Return <result>: pooled matrix.
    '''
    # Define the doubly ended queue, that will
    # behave like a monotonic doubly ended queue.
    dq = deque()
    res = []

    # Iterate from i = 0 to i = k - 1.
    for i in range (k):
        # Pop out all elements from tail
        # which are smaller than a[i].
        while(dq and
            arr[dq[-1]] <= arr[i]):
            # Removing from rear (tail side).
            dq.pop()

        # Add the current element.
        dq.append(i)
    

    # Iterate from i = k to i = n - 1.
    for i in range (k, n):
        # Print the element at the head of the queue. 
        res.append(arr[dq[0]])

        # Remove the elements which no longer
        # lies in the window.
        while(dq and dq[0] <= i - k):
            # Removing from front (head side).
            dq.popleft()

        # Pop out all elements from tail
        # which are smaller than a[i].
        while(dq and arr[dq[-1]] <= arr[i]):
            # Removing from rear (tail side).
            dq.pop()

        # Add the current element.
        dq.append(i)
    
    # Print the element at head of the queue
    # that is maximum element of last window.
    res.append(arr[dq[0]])
    return res


# Driver code

#creating a numpy array
arr = np.array([[  20,  200,   -5,   23],
       [ -13,  134,  119,  100],
       [ 120,   32,   49,   25],
       [-120,   12,   9,   23]])

r =[]
for x in arr:
    #calculate the 1D sliding window maximum for each row
    r.append(maxPool(x, len(x), 2))

#storing the column of previous rows in a list
col = list(zip(*r))
fin = []
for x in col:
    #calculate the 1D sliding window maximum for each column
    fin.append(maxPool(x, len(x), 2))

#transposing the final answer and printing it
y = np.array(fin)
ans = np.transpose(y)
print(ans)
