import 'reverse.dart';

void main(){


//print(reverseArray(arr));
print(isStrPalindrome('abd'));


}


void printFunction(int i , int n){
  if(i>n) return ;

  print('$i\n');

  printFunction(i+=1,n);
}


int  sumOfInt( int n){


  if(n==0) {return 0;}
 return n+ sumOfInt(n-1);


}

int fact(int n){
  if(n==1){
return 1;
  }

  return n*fact(n-1);
}

String reverseArray(List<String> array){
  String temp='';
  int length= array.length-1;
// [1,2,3,4,5]
// [5,4,3,2,1]
int i=0;
  while(length>i){
    temp=array[length];
    array[length]=array[i];
    array[i]=temp;
    length-=1;
    i+=1;
  }
  return array.join('');
}

List<int> revreseArr(List<int> arr, int right, int left){

  if(right>left){
    int temp=arr[right];
    arr[right]=arr[left];
    arr[left]=temp;
    revreseArr(arr, right-1, left+1);
    }
    return arr;

}

bool isStrPalindrome(String text){

  List<String> spliteddata=text.split('');

  String revrsetext=reverseArray(spliteddata);

  if(revrsetext.contains(text)){
    return true;
  }

  return false;

}