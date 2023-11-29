

if __name__=="__main__":
    hash = [0 for x in range(8)]

    values =  [1,1,2,3,4,5,6,7,5,3,4]
#precompute
    for i in values:
        hash[i]+=1
      
        #isthash.append(value)

    print(hash)
#fetching
    print(hash[6])
