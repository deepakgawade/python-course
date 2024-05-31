void main(){

 List<int> list=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1];

 print(zerosAtBack(list));

}

List<int> zerosAtBack(List<int> data){

  for(int i=0; i<data.length;i++){
    if(data[i]==0){
      int temp=data[i];
      for(int j=i;j<data.length-1;j++){
        data[j]=data[j+1];
      }
      data[data.length-1]=temp;
    }
  }
  return data;
}