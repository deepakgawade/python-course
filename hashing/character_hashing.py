if __name__=="__main__":
    lsitOfcharacters=["a","b","b","c","z","e","f","z","k","a"]

    hash=[i for i in range(26)]
#precompute
    for ch in lsitOfcharacters:
         value=ord(ch) - ord("a")

         hash[value]+=1
#fetch
    print(hash[0])