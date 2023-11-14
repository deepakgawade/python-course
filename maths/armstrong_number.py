def isArmstrong(vale):
    num=vale
    sum=0
    length=len(str(vale))
    while(num%10!=0):
        
        sum=sum+((num%10)**length)

        num=int(num/10)
    if vale==sum:
        return True
    else:
        return False
    
if __name__=="__main__":
    print(isArmstrong(2))
    print(isArmstrong(10))
    print(isArmstrong(153))
    print(isArmstrong(1634))