def countDigit(value):
    num=value
    count=0
    while(num%10!=0):
        count+=1
        num=int(num/10)
    
    return count
if __name__=="__main__":
    print(countDigit(1))