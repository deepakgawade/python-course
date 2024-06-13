import 'dart:math';

void main(){

  List<int> arr=[2,3,5,1,9];
  int k=10;
  int len=0;

  for(int i=0;i<arr.length;i++){
    int sum=0;

//webwer

    for(int j=0;j<i;j++){

      sum=sum+arr[j];
      if(sum==k){
      len=max(len, j+1);
    }

    }



  }
  print(len);

}