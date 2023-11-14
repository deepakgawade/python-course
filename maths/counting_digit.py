import math

def countDigit(value):
    num=value
    count=0
    while(num%10!=0):
        count+=1
        num=int(num/10)
    return count

def withLog(value):
    digits= math.floor(math.log10(value)+1)
    return digits


if __name__=="__main__":
    print(countDigit(54636))
    print(withLog(54636))