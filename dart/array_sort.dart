void main() {

  
  List<int> arr1 = [1,2,3,4, 5];
  List<int> arr2 = [2,3,4,4,5];
  
  List<int> answer=[];
  
  int i=0;
  int j=0;
  
  int n1 = arr1.length;
  int n2 = arr2.length;
  
  // 
  while(i<n1 && j<n2){
    
    if ( arr1[i]<=arr2[j]){
      if(answer.isEmpty){
          answer.add(arr1[i]);
      }
     else if(answer.last==arr1[i]){
        //no add
      }else{
        answer.add(arr1[i]);
      }
      i++;
      
    }else{
         if(answer.last==arr2[j]){
        //no qadd
      }else{
        answer.add(arr2[j]);
      }
      j++;
    }
  }
  
  while(i<n1){
      if(answer.last==arr1[i]){
        
      }else{
        answer.add(arr1[i]);
      }
      i++;
    
  }
  
    while(j<n2){
      if(answer.last==arr2[j]){
        //no add
      }else{
        answer.add(arr2[j]);
      }
      j++;
    
  }
  
  print(answer);
}
