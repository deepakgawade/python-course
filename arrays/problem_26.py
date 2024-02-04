 
from collections import Counter

def bruteElement(arr):

    answers=[]
    n=len(arr)
    print(n)
    minelemsts=n//3
    print(minelemsts)


    for i in range(n):
        size=len(answers)
      
        if  size==0 or answers[0]!=arr[i]:
            count=0

            for j in range(n):
                if arr[i]==arr[j]:
                    count+=1

            if count>minelemsts:
                answers.append(arr[i])

        if size==2:
                break
    return answers


def betterElement(arr):
     
     n=len(arr)
     minleemts=n//3
     counter=Counter(arr)
     answer=[]


     for num, count  in counter.items():
          
          if count>minleemts:
               answer.append(num)
               

     if len(answer)==0:
          return -1
     else:
          return answer


def mooreElement(arr):
     answer=[]
     count1=0 
     count2=0
     el1, el2=float('-inf'),float('-inf')
     n=len(arr)
     for i in range(n):
        if count1==0 and el1!=arr[i]:

            el1=arr[i]
            count1=1
        elif count2==0 and el2!=arr[i]:
            el2=arr[i]
            count2
        elif el1==arr[i]:
            count1+=1
        elif el2==arr[i]:
            count2+=1
        else:
            count2-=1
            count1-=1
     cont1,cont2=0,0
     for i in range(n):
         if arr[i]==el1:
             cont1+=1
         if arr[i]==el2:
             cont2+=1

     minelemsts=n//3
     if cont1>minelemsts:
         answer.append(el1)
     if cont2>minelemsts:
         answer.append(el2)
     return answer

             
    
if __name__=="__main__":
    elemts=[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
    print(mooreElement(elemts))