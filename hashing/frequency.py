if __name__=="__main__":
    lsitOfcharacters=[2,5,5,10,0,10,2,5,0,9,8,1,1,9]

    hash=[0 for i in range(11)]
#precompute
    for ch in lsitOfcharacters:
         #value=ord(ch) - ord("a")

         hash[ch]+=1
#fetch
    maxelefre=0
    smallelefre=0
    maxele=0
    for i  in lsitOfcharacters:
        if maxelefre<hash[i]:
            maxelefre=hash[i]
            maxele=i


        if smallelefre<hash[i]:
            maxelefre=hash[i]
            maxele=i
         
        print(f"{i} {hash[i]}times ")