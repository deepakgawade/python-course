import sys

def fact(n):
    if n<0:
        return "Factorial of negative number is not defined"
    if n==0:
        return 1
    return n*fact(n-1)
if __name__=="__main__":
    print(fact(-5))
    print(sys.getrecursionlimit())