# You have N rectangles. A rectangle is golden if the ratio of its sides is in between [1.6,1.7] , both inclusive. Your task is to find the number of golden rectangles.

# Input format

# First line: Integer N denoting the number of rectangles
# Each of the N following lines: Two integers W,H denoting the width and height of a rectangle
# Output format



N=int(input())

def isGoldenRectangle( _range, _width, _height):

    ratio =_width/_height
    ratio2 =_height/_width

    if (ratio >= _range[0] and ratio <=  _range[1]) or (ratio2 >= _range[0] and ratio2 <= _range[1]):
            
        return 'Golden'

    return -1
    



count=0

for i in range(N):

    arr = list(map(int,input().split(' ')))

    rect=isGoldenRectangle([1.6,1.7],arr[0],arr[1])
    if rect=='Golden':
        count=count+1
print(count)



