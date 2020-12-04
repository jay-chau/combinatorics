import numpy as np

def permutations(r,n):
    '''
    Returns an array of all possible permutations of r and n
    where r is the number of samples taken 
    and n is the number of possible values of each sample.
    '''
    print("Array Size: {}x{}".format(n**r, r))
    y = np.empty([n**r, r])   
    for i in range(r):
        x = [a for a in range(n) for b in range(n**i)] * (n ** (r-1-i))
        y[:,i] = x
        print("Completed {} of {} columns".format(i+1, r))
    return y