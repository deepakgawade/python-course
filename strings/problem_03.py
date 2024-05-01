def largestOddNumber(str):

    n=len(str)

    j=n-1

    while 0<=j:

        num=int(str[j])

        if num%2==1:

            return str[0:j+1]
        j-=1
        
    return ''

if __name__=="__main__":
    number='35427'
    print(f"Largset ood number is: {largestOddNumber(number)}")
