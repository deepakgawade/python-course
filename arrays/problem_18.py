def generateAllPermutations(arr):
    n=len(arr)
   
    ans_list=[0]


    ds=[]
    freq=[False for i in range(n)]
    recurPermute(arr, ds, ans_list, freq,)
    
def recurPermute(numbers, ds, ans_list, freq,):
   
    if len(ds)==len(numbers):
        ans_list.append(ds)
     
        return
    
    for i in range(len(numbers)):
       
        if not freq[i]:

            freq[i]=True
            ds.append(numbers[i])

            recurPermute(numbers, ds, ans_list, freq,)
            ds.pop(len(ds)-1)

            freq[i]=False

 

def recursive_function(my_list, depth):
    if depth > 0:
        my_list.append(depth)
        recursive_function(my_list, depth - 1)



   
if __name__=="__main__":

    elements=[1,2,3]
    print(generateAllPermutations(elements))
    

    # Example usage
    my_list = [0]
    recursive_function(my_list, 5)
    print(my_list)
    




