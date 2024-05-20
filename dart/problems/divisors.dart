import 'dart:math';

void main(){
  
  allDivisorsBySymmetri(10).forEach(print);

}


List<int> allDivisors(int n){
  List<int> divisors=[];
 int i=1;
  while(i<=n){

    if (n%i==0) divisors.add(i);

    i+=1;
  }

  return divisors;
}



List<int> allDivisorsBySymmetri(int n){
  List<int> divisors=[];

  int sqrtnumber=sqrt(n).round();

  int i=1;
  while(i<=sqrtnumber){

    if (n%i==0){ 
      divisors.add(i);

      if(n~/i!=i){
        divisors.add(n~/i);
      }
      }

    i+=1;
  }

  return divisors;
}

