import 'dart:math';

void main(){
  int n=11;

  print(n.isPrime());

}

extension FindPrime on int{
  bool isPrime(){


  int sqrtNumber=sqrt(this).round();
  int i=1;
  int count=0;
  while(i<=sqrtNumber){

      if(this%i==0){
        count+=1;

        if (this~/i!=i){
          count+=1;
        }

        }
  i+=1;
  }
  if (count==2)return true;


  return false;
}

}
