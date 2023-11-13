def pallindrome(value):
    num = value
    newValue=""
    while(num%10!=0):
        newValue= newValue+str(num%10)
        num=int(num/10)

    
    if newValue == str(value):
        return True
    else:
        return False
if __name__=="__main__":
    print(pallindrome(12345654321))