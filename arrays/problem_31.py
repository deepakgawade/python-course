def bruteMergeOvelapping(arr):

    n=len(arr)
    arr.sort()
    answer=[]

    for i in range(n):
        start = arr[i][0]
        end= arr[i][1]
        if answer and end<=answer[-1][1]:
            continue

        for j in range(i+1,n):

            if arr[j][0]<=end:
                end=max(end, arr[j][1])
      
            else:
                break
        answer.append([start,end])

    return answer





if __name__=="__main__":
    elemst=[[1,3],[2,6],[8,10],[15,18]]
    print(bruteMergeOvelapping(elemst))

