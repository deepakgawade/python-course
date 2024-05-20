
import 'dart:math';
void main(){

print("${armstrongNumber(371)}  ${armstrongNumber(153)}");

}


bool armstrongNumber(int number){

  int digit=0;
  int number3=number;
  int number2=number;

  while(number%10!=0){

    digit+=1;
    number=number~/10;

  }

  num sum=0;

  while(number2%10!=0){
    int num =number2%10;
    sum =sum+pow(num,digit);
    number2=number2~/10;

  }

return sum as int ==number3;

}