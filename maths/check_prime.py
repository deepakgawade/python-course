def allDivisorslist(value):
    divisors=[]
   
    for i in range(1,int(value**0.5)+1):
        if value%i==0:
            divisors.append(i)
            if i!=value/i:
                divisors.append(int(value/i))

    

    return len(divisors)<3
if __name__=="__main__":
    print("given number is prime", allDivisorslist(6))


