void main(){

 List<int> list=[1 ,0 ,0 ,3 ,0 ,4 ,0 ,1];

 print(zerosAtBackR(list));

}

List<int> zerosAtBack(List<int> data){

  for(int i=0; i<data.length;i++){
    if(data[i]!=0){
      int temp=data[i];
      for(int j=i
      +1;j<data.length-1;j++){
        data[j]=data[j+1];
      }
      data[data.length-1]=temp;
    }
  }
  return data;
}

List<int> zerosAtBackR(List<int> data){

  int j=0;

  for(int i=0; i<data.length;i++){
    
    if (data[i]!=0){

      int temp= data[j];
      data[j]=data[i];
      data[i]=temp;


      j+=1;

    }


  }
  return data;
}

//[1 ,0 ,0 ,3 ,0 ,4 ,0 ,1]
//[1 ,3 ,0 ,0 ,0 ,4 ,0 ,1]


