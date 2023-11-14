import math

def allDivisors(value):
    divisors=[]
   
    for i in range(1,int(value/2)+1):
        if value%i==0:
            divisors.append(i)
    divisors.append(value)

    return divisors


def allDivisorslist(value):
    divisors=[]
   
    for i in range(1,int(value**0.5)+1):
        if value%i==0:
            divisors.append(i)
            if i!=value/i:
                divisors.append(int(value/i))

    return divisors
    

if __name__=="__main__":
    print(allDivisorslist(10))

    print(allDivisorslist(36))