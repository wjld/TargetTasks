'''n is a fibonacci number if and only if one of
5*n**2 ± 4 is a perfect square'''

def isPerfectSquare(n):
    return n**0.5 == int(n**0.5)
 
def isFibonacci(n):
    return isPerfectSquare(5*n**2 + 4) or isPerfectSquare(5*n**2 - 4)

n = input("insert a number: ")
if (isFibonacci(int(n))):
    print (n,"is a fibonacci number")
else:
    print (n,"is a not fibonacci number ")