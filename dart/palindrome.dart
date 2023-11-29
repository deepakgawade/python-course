  bool isPalindrome(int num){
  int value=num;
  int newnum=0;
  while(value%10!=0){
    newnum=newnum*10+value%10;
  }
  if(num==newnum){
    return true;
  }
  return false;
}

  int romanToInt(String s) {
   Map<String, int> data = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  };
    
    var splitnum=s.split("");
    print(splitnum);
    int num=0;
    for (int i=splitnum.length-1;0<=i;i--){
      
      
       if(num<=data[splitnum[i]]!.toInt()){
         
      num=num+data[splitnum[i]]!.toInt();
         
    }else{
         
            num=num-data[splitnum[i]]!.toInt();
       }
      
    }
    
 
   
     print(num);
    
    return 0;
  }

void main(){
  print(isPalindrome(1001));
}