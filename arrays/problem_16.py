

def buysellstock(arr):
    n= len(arr)
    low_index=0
    high_index=0
    low,high = arr[0],0
 
    for i in range(n):
        if arr[i]<low:
            low=arr[i]
            low_index=i
           

    for j in range(low_index, n):
        if arr[j]>high:
            high=arr[j]
            high_index=j

    print(f"person Should buy on {low_index+1}th day abd sell on {high_index+1}th day, profit will be {high-low}")
        
    pass

def optimizeApproach(arr):
    n=len(arr)
    minPrice = float('inf')
    maxPro=0
    for i in range(n):
        minPrice= min(minPrice, arr[i])
        maxPro=max(maxPro, arr[i]-minPrice)

    return maxPro

if __name__=="__main__":
    elements=[7,1,5,3,6,4]
    buysellstock(elements)
    print(optimizeApproach(elements))