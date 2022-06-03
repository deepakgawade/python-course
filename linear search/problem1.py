import math

# Write your code here

N = int(input())

def hex2sum(a):

    sum_a = sum_i = 0

    a = hex(a)[2:]

    dic = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

    for i in a:

        try:

            sum_i += int(i)

        except:

            sum_a += dic[i]

    return sum_i + sum_a


 

for i in range(N):

    arr = list(map(int,input().split(',')))

    count = 0

    for i in range(arr[0], arr[1]+1):

        if (math.gcd(i, hex2sum(i)) > 1):

            count += 1

        print(count)