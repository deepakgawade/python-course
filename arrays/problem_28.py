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
                    


                elif sum<x:
                    k+=1
                else: 
                    l-=1



