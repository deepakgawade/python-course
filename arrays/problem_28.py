def  better4Sum(arr,x):

    n=len(arr)

    sttAnser=set()


    for i in range(n):
        for j in range(i+1,n):
            stt=set()

            for k in range(j+1, n):
                sum = arr[i]+arr[j]+arr[k]
                fourth=x-(sum)
                if fourth in stt:
                    temp= [arr[i],arr[j],arr[k],fourth]
                    temp.sort()
                    sttAnser.add(tuple(temp))
                    

                stt.add(arr[k])
  

    
def optimal4Sum(arr, x):

    n=len(arr)
    arr.sort()
    answer=[]

    for i in range(n):

        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,n):
            if j >i+1 and arr[j]==arr[j-1]:
                continue
            k=j+1
            l=n-1

            while(k<l):
                sum = arr[i]+arr[j]+arr[k]+arr[l]
                if sum==x:

                    temp=[arr[i],arr[j],arr[k],arr[l]]
                    answer.append(temp)
                    k+=1
                    l-=1
                    while(k<l and arr[k]==arr[k-1]):
                        k+=1
                    while(k<l and arr[l]==arr[l+1]):
                        l-=1


                elif sum<x:
                    k+=1
                else: 
                    l-=1

    return answer

if __name__=="__main__":
   elemts= [1,0,-1,0,-2,2]
   x=0
   anser= optimal4Sum(elemts,0)

   for item in anser:
       print(item)



