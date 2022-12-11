import numpy as np
def maxPool(arr,k):
    '''Non-overlapping pooling on 2D or 3D data.

    <arr>: ndarray, input array to pool.
    <k>: tuple of 2, kernel size in (ky, kx).

    Return <result>: pooled matrix.
    '''

    m, n = arr.shape[:2]
    ky,kx=k
    _ceil=lambda x,y: int(np.ceil(x/float(y)))

    ny=m//ky
    nx=n//kx
    mat_pad=arr[:ny*ky, :nx*kx, ...]

    new_shape=(ny,ky,nx,kx)+arr.shape[2:]

    result=np.nanmax(mat_pad.reshape(new_shape),axis=(1,3))

    return result

arr = np.array([[  20,  200,   -5,   23],
       [ -13,  134,  119,  100],
       [ 120,   32,   49,   25],
       [-120,   12,   9,   23]])

k = [2,2]
print(maxPool(arr, k))
