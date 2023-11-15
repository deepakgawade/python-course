def sumOfNum(n):
    if n==0:
        return 0
    return n + sumOfNum(n-1)


def optimalsum(n):
   sum=n*(n+1)/2
   return sum


if __name__=="__main__":
    
  print(sumOfNum(10))
  print(optimalsum(10))