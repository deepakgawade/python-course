
import 'dart:ffi';

import 'array_sort.dart';

Map<String, String> map={'1':"one",'2':"Two"};








class Square implements Shape{
  final double side;

  Square({required this.side});
  
  @override
  void area() {
   print("area of square is ${ side*side}");
  }

}

class Circle implements Shape{
final double radius;

  Circle({required this.radius});



  @override
  void area() {
   print("area of circle is ${3.14*radius*radius}");
  }
}
// factory cnstructor is used return a subtype  
abstract class Shape {
  Shape();
 factory Shape.ofType(String type,List<double> list){
    if (type =='circle')return Circle(radius: list[0]);
    if(type=='square') return Square(side: list[0]);

    throw ArgumentError("Unknown ${type}");
  }

  void area();
}


void main(){
  List<int> list= [1,2,3,3,5,4,5];
  Set<int> set={};

  //O(N)
  //O(N)


Shape circle=Shape.ofType('circle',[5]);
Shape square=Shape.ofType('square',[5]);

circle.area();
square.area();





  for(int i=0;i<list.length;i++){
    set.add(list[i]);

  }
  list=set.map((element) =>element).toList();

 // list.forEach((element) {print(element);});

  // item in the list is empty
  List<String> s=['asd','asdasd','adsas',];
  bool emptyExistInString=s.any((element) => element.contains('f'));

 // print(emptyExistInString);

 //factory constructor to return its sub type


}



