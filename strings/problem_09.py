def checkOrder(s):

    count,maxValue=0,0

    for i in s:

        if i=="(":
            count+=1
        elif i==")":
            maxValue=max(maxValue,count)
            count-=1
    return maxValue

if __name__=="__main__":
    print(checkOrder("(1+(2*3)+((8)/4))+1"))


    