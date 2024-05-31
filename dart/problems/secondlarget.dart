import 'dart:math';

void main(){
  List<int> elements=[1,2,4,7,7,5];

secondLargestAndSmallest(elements);

}

List<int> secondLargestAndSmallest(List<int> list){
List<int> secondSmallLarge=[];


int mini=double.maxFinite.toInt();
int maxi=-double.maxFinite.toInt();

int secondlarge=-double.maxFinite.toInt();
int secondSmall=double.maxFinite.toInt();

for(int i=0;i<list.length;i++){

  if(mini>list[i]){
    secondSmall=mini;
    mini=list[i];
    
  }else if (secondSmall>list[i] && list[i]!=mini){
    secondSmall=list[i];

  }

    if(maxi<list[i]){
    secondlarge=maxi;
    maxi=list[i];
    
  }else if (secondlarge<list[i] && list[i]!=maxi){
    secondlarge=list[i];

  }



}
print("minimum: ${mini}, maximum:${maxi}, secondLarge: ${secondlarge}, secondSmall: ${secondSmall}");
  return secondSmallLarge;

}