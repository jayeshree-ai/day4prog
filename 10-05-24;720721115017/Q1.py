def fib(n):

    if n <= 1:

        return n

    return fib(n-1) + fib(n-2)
 

def countWays(s):

    return fib(s + 1)
 
 

s=2
print (countWays(s))
s1=3
print(countWays(s1))
