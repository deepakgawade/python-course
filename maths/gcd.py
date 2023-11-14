def getGCD(num1, num2):
    gcd=0
    for i in range(1,min(num1, num2)+1):
        if num1%i==0 and num2%i==0:
            gcd=i
        
    return gcd

def optGCD(nm1,nm2):
    if nm2==0:
        return nm1
    return optGCD(nm2, nm1%nm2)



if __name__=="__main__":
    print(getGCD(21,63))
    print(optGCD(63,21))


    