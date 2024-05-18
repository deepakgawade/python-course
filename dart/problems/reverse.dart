void main(){

print(reverse(12345));

}

int reverse(int number){
int reversed=0;
  while(number%10!=0){
    int num=number%10;

        reversed=reversed*10+num;
        number=number~/10;

  }

  return reversed;

}