void main() {
  //545
  
  //545, 151, 34543, 343, 171, 48984
  
  print(palindrome(5451));
  
  
  
 
}

bool palindrome(int number){
  
  String num1= number.toString();  
  int numlen= num1.length;
  int reversed=0;

  int numd=number;
  while(0<numlen){
    
    int num = numd%10;
    reversed= (reversed*10) + num;
    numd= numd ~/10;
    
    numlen-=1;
    
  }

  if(number == reversed){
    return true;
  }
  
  return false;
  
}