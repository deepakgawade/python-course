def reverseNum(value):
    num=value
    newValue=""
    while(num%10!=0):
        newValue=newValue+str(num%10)
        num=int(num/10)
    return newValue


if __name__=="__main__" :
    print(reverseNum(123456))


    