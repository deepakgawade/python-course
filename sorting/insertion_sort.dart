void main(){
  List<int> list=[13,46,24,52,20,9];


  for(int i=0; i<list.length;i++){
    int j=i;
  
    while(j>0 && list[j-1]>list[j]){
      int temp= list[j-1];
      list[j-1]=list[j];
      list[j]=temp;
      j-=1;
    }
  }

  print(list);
}