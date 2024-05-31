import 'dart:math';

void main(){
  List<int> elements=[2,5,1,3,0,100];
  print(largestElement(elements));

}

int largestElement(List<int> list){

  int large=-double.maxFinite.toInt();

  for (int i=0;i<list.length;i++){

    large=max(list[i], large);
  }

  return large;

}