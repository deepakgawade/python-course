def singleElementInArray(array):
    #(even,odd),(even,odd),(element)(odd,even)(odd,even)

    n=len(array)
    low=0
    high=n-1
#edge cases
    if n==1:return array[0]

    if array[0]!=array[1]: return array[0]

    if array[n-1]!=array[n-2]: return array[n-1]

    while low<=high:

        mid =(low+high)//2
        #chech if elementv is single
        if array[mid]!=array[mid+1] and array[mid]!=array[mid-1]:
            return array[mid]
        
        if (mid%2==0 and array[mid]==array[mid+1] ) or  (mid%2==1 and array[mid]==array[mid-1] ) :
            low =mid+1

        else: 
            high=mid-1



if __name__=="__main__":
    elelmts=[1,1,2,2,3,3,4,5,5,6,6]
    print(singleElementInArray(elelmts))

        
