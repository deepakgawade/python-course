import 'dart:math';

void main(){

  List<int> list=[1, 1, 0, 1, 1, 1];
  List<int> list2=[1, 0, 1, 1, 0, 1];
  print(maxConcecutiveOne(list2));
}

int maxConcecutiveOne(List<int> data){

  int maxi=0;
  int count=0;

  for (int i=0;i<data.length;i++){
    
    if (data[i]==1){
      count+=1;
    }else{
      maxi=max(maxi, count);
      count=0;
    }
  }
   maxi=max(maxi, count);
  return maxi;
}