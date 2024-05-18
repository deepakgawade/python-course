void main(){
print(numOfDigits(7798182293));
}

int numOfDigits(int number){
int count=0;

while (number%10!=0){

  int num=number%10;

  count+=1;

  number=number~/10;





}


  return count;
}