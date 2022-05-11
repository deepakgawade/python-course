class BinarySearch:
    def sqrt(self, x):
    
        start = 1
        end = x  
        while (start <= end) :
            mid = (start + end) // 2
         
        # If x is a perfect square
            if (mid*mid == x) :
                return mid
             
        # Since we need floor, we update
        # answer when mid*mid is smaller
        # than x, and move closer to sqrt(x)
            if (mid * mid < x) :
                start = mid + 1
                ans = mid
             
            else :
             
            # If mid*mid is greater than x
                end = mid-1
             
        return ans
if __name__=="__main__":
    binary=BinarySearch()

    num=  binary.sqrt(16)
    print(num)