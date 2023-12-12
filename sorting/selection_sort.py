if __name__=="__main__":
    elements= [19,54,86,10,8,43]
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

        



   

    
        




    