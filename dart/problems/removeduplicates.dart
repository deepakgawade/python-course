void main(){
  List<int> data=[1,1,2,2,2,3,3];
  print(inPlaceRemoveDuplicates(data));

}
List<int> inPlaceRemoveDuplicates(List<int> list){
  int i=0;
  int j=1;
  int n=list.length;


  while(j<n){

    if(list[i]!=list[j]){
      i+=1;
   

    list[i]=list[j];

    
  }
  j+=1;
 
}
 return list.sublist(0,i+1);
}


List<String> removedDuplicates(List<int> list){

  List<String> answer=[];

  int len=list.length;

  int i=0;
  print(len);
  while(i<len ){

    if(answer.isEmpty){

      answer.add("${list[i]}");
      print(answer);
  

    }
    else if(
      
      answer.last.compareTo(list[i].toString())!=0){
print(answer);
      answer.add("${list[i]}");
  
      
      }

  i+=1;


  }

  int remainingLength=len-answer.length;

  for(int j=0;j<remainingLength;j++){
     answer.add("_");
  }


  return answer;
}