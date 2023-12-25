def removeDuplicate(arr):
    setarr=set(arr)
    print(setarr)

    noduparr=list(setarr)

    for i in range(len(noduparr)-1, len(arr)):
        print(i)
        noduparr.append("_")

    print(noduparr)
    # for i in range(len(arr)-1):rmeove dupl
    #     if arr[i]==arr[i+1]:
    #O(nlogn)



def pointRemoveDuplicate(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            print(arr[j])
            i+=1
            arr[i]=arr[j]
        
        else:
            pass

    newSize=i+1

    for k in range(newSize, len(arr)):
        arr[k]="_"

    print(arr)
    #O(n)
if __name__=="__main__":
    elements=[1,1,2,2,4,5,33,33]
    pointRemoveDuplicate(elements)

    

