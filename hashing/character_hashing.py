if __name__=="__main__":
    lsitOfcharacters=["a","b","b","c","z","e","f","z","k","a"]

    hash=[i for i in range(26)]

    for ch in lsitOfcharacters:
         value=ord(ch) - ord("a")

         hash[value]+=1

    print(hash[0])