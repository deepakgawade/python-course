import 'dart:math';

void main(){
List<int> trees=[9,4,7];
List<int> persons=[2,1];
closetDistanceForPerson(trees,persons);
    // int smallUnit=-double.maxFinite.toInt();

    // if (smallUnit<-1){
    //   print(true);
    // }else{
    //        print(false);

    // }



}


List<int> closetDistanceForPerson(List<int> trees, List<int> persons){

  List<int> unitDistanceOfAll=[];

  
  for(int i=0;i<persons.length;i++){


    int smallUnit=double.maxFinite.toInt();

    print("Person ${persons[i]}");

    for (int j=0;j<trees.length;j++){

    int ans=0; 

      if(persons[i]>trees[j]){

        ans=persons[i]-trees[j];

      }else{

          ans=trees[j]-persons[i];

      }
       
      print(ans);
      

      smallUnit=min(ans, smallUnit);


    }
    unitDistanceOfAll.add(smallUnit);
  }

print(unitDistanceOfAll);

  return unitDistanceOfAll;


}