#calculator.py: by Renato Eschini

# define 'sum' by increment by n-times '1'
def sum(m, n): 
    times = abs(n) # number of iterations
    inc = 1 if n > 0 else -1 # check if I need to sum or sub (if n is negative)
    for i in range(times): # loop 'times' for increment
        m += inc # increment
    return m # return result
 
 
# define 'div' by subtracting n 'times', while tmp result is equal or less zero,
# so return 'times'. If n i zero rise exception
def divide(m, n):
    if n == 0: raise Exception('Divide by zero')      
    times = 0 # result
    sign = 1 if ((n > 0) == (m > 0)) else -1 # if the sign is not equal, the sign is negative
    tmpM = abs(m) # ignore sign
    tmpN = abs(n) # ignore sign
    while tmpM > 0: # iterate while the tmpM var is positive, when is equal or less zero, exit while
        tmpM -= tmpN # subtract tmpN
        times += 1 # accumulate which time the tmpN is subtracted from tmpM
    return times * sign # return result with sign