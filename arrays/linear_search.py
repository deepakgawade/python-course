def linearSearch(arr, element):

    for i in range(len(arr)):
        if arr[i]==element:
            print(i)
            return
    print(-1)

   

if __name__=="__main__":
    elements= [1,2,3,4,5,67,7,]
    linearSearch(elements, 20)