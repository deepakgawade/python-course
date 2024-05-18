void main(){
  print(gcdOfNumbers(15, 20));
  print(gcdOfNumbers(20, 15));

}


int gcdOfNumbers(int a, int b){

  int gcd=1;

  if(b<a) return gcdOfNumbers(b, a);

  for(int i=1;i<a;i++){

    if(a%i==0 &&b%i==0){
      gcd=i;
    }

  }

  return gcd;
}

//according to euclideans principals 

int gcdWithEuclidean(int a, int b){

  while(a>0 && b>0){

    if(a>b){  
      //same like subtacting 
      a=a%b;

    }else{
      b=b%a;
    }
  }

  if (a==0){
    return b;
  }
  return a;

}