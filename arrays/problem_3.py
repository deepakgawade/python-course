def checkSorted(arr):
    count=0
    for i in range(len(arr)-1):
        if arr[i]<=arr[i+1]:
            print(i)
        else:
            count+=1


    if count==0:
        return True
    else:
        return False
    
if __name__=="__main__":
    elemts=[34,6,75,23,989,2,10,0]
    elemts2=[1,2,3,4,6,8,9,0]

    print(checkSorted(elemts2))