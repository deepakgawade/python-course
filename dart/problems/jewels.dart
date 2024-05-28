void main() {

  
  String jewel="aAAA";
  String stone="aAAbbbb";

  
  print(jewsCount(jewel,stone));
}

int jewsCount(String jewel,String stone){
  
 Set<String> jews=jewel.split("").toSet(); 
    
  List<String>stones=stone.split("");
  
  int jewelCount=0;
  
  for (final j in jews) {
    
    for (int k =0; k<stones.length;k++){
      
      if (j.compareTo(stones[k])==0){
        
        jewelCount+=1;
      }
      
    }
    
  }
  return jewelCount;
  
}
