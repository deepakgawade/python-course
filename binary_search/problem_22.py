def allocateMinimumPagesBooks(arr,nofStudent):

    n=len(arr)
    if nofStudent>n:
        return -1
    low=max(arr)
    sumOfPages=0
    for i in range(n):
        sumOfPages+=arr[i]
    high=sumOfPages

    countStudent=0
    #here we cn use binary search:
    for pages in range(low,high+1):

        countStudent= countOfStudentWithBooks(arr, pages)

        if countStudent==nofStudent:
            return pages
        
def countOfStudentWithBooks(arr, pages):
    n=len(arr)
    student=1
    pagesStudent=0
    for i in range(n):

        if arr[i]+pagesStudent<=pages:

            pagesStudent+=arr[i]

        else:
            student+=1
            pagesStudent=arr[i]

    return student


if __name__=="__main__":

    elements=[12, 34, 67, 90]
    students=2

    print(allocateMinimumPagesBooks(elements,students))

        




