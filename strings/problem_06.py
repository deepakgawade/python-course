
def rotateArray(arr):

    temp=''
    x=len(arr)
    print(x)

    for i in range(x-1):

        temp=arr[i]
        arr[i]=arr[i+1]
        arr[i+1]=temp

    print(f"roated {''.join(arr)}")
    return arr


def checkSymbol(arr,target):

    if len(arr)!=len(target):
        return False

    k=len(arr)

    splitedArray=list(arr)


    while k>0:

        splitedArray=rotateArray(splitedArray)

        if ''.join(splitedArray) == target:

            return True
        

    return False


def rotateString(s,t):
    temp=''

    temp=s+s

    if temp.count(t)>0:
        return True
    return False


if __name__=="__main__":

    #print(checkSymbol('abcde','cdeab'))
    print(rotateString('abcde','cdeab'))