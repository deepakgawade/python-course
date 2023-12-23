def removeDuplicate(arr):
    setarr=set(arr)
    print(setarr)

    noduparr=list(setarr)

    for i in range(len(noduparr)-1, len(arr)):
        print(i)
        noduparr.append("_")

    print(noduparr)
    # for i in range(len(arr)-1):
    #     if arr[i]==arr[i+1]:

if __name__=="__main__":
    elements=[1,1,2,2,33,33,4,5]
    removeDuplicate(elements)
    

