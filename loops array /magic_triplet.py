if __name__=="__main__":
    def countTriplet(arr):
        count=0
        for i in range(1,len(arr)):
            sm=0
            gt=0

            for j in range(i):
                if arr[j]<arr[i]:
                    sm+=1
            
            for k in range(i,len(arr)):
                if arr[k]>arr[i]:
                    gt+=1
            count+=gt*sm
        return count;

    #get array
    data=[1,3,4,2]
    data2=[1,3,2]
    #if items given are in ascending order then permutaion of selecting three items will be
    #len(data)!/(len(data)-3)! then divide same by 6(since the permutation for 3 item is 6)

    ans=countTriplet(data)
    print("This array has {} magical triplet".format(ans))
       
