
def selection_sort(elements):
    temp=0
    print(elements)
    for i in range(6):
        min=i
        for j in range(i,5):
            if elements[j]<elements[min]:
                min=j
        
        temp=0

        temp=elements[i]
        elements[i]=elements[min]
        elements[min]=temp

    print(elements)
#time complexity is O(n2)
    #direct swaping with last min largest element
def bubble_sort(elements1):
    temp=0
    for i in range(6):
        for j in range(0,5-i):

            if elements1[j]>elements1[j
                                      +1]:
                temp=elements1[j]
                elements1[j]=elements1[j+1]
                elements1[j+1]=temp
        
    print(elements1)
    #time complexity will be O(n2)
    # adjanent swapping

def insertion_sort(element2):

    temp=0
    for i in range(6):
        j=i

        while j>0 and element2[j-1]>element2[j]:
            temp=element2[j]
            element2[j]=element2[j-1]
            element2[j-1]=temp

            j-=1

    print(element2)


    

    

if __name__=="__main__":
    elements= [19,54,86,10,8,43]
   # selection_sort(elements)
    #bubble_sort(elements)
    insertion_sort(elements)
 

        



   

    
        




    