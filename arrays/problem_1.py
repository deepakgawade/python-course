
def maxValue(a,b): 
    if a <= b:           
        return b
    else:
        return a

def largest(arr, i, n, maxV):
    if i>n:
        print(maxV)
        return 
    maxV = maxValue(maxV, arr[i])
    largest(arr, i+1, n, maxV )
        
 
    

      
        
    
    

if __name__=="__main__":

    elements= [19,54,86,10,8,43]
    max=elements[0]

    # for i in range(len(elements)-1):
    #     if max<elements[i]:
    #         max=elements[i]
    # print(max)
largest(elements, 0, len(elements)-1,max)
