///import 'dart:async';
//take while and skipwhile

//dart is type safe we can use var 

int fibonaci(n){
  if (n==0||n==1) return n;
  return fibonaci(n-1) + fibonaci(n-2);
}

// enhanced enums

enum Planet{
  
  earth(name: "Earth",desciption: "It is the only habitual planet"),mercury(name: "Mercury",desciption: "These planet has potetila for life.");
const Planet({required this.name, required this.desciption});
void describes(){
  print(this.desciption);
}
final String name;
final String desciption;

}

//dart only has single inheritance

//mixins are used  for providing functionality of code resuse 

//multiple mixins can be used with keyword for class

mixin Animal{
final bool canfly=false;

void doesFly(){
  print("Animal fly ${canfly}");
}
}
void main(){

  Iterable<int> items=[1,2,3,4,55,5,4,3,2,];

  print(items.firstWhere((element) => element%11==0));

  print(items.takeWhile((value) => value!=55));
  print(items.skipWhile((value) => value!=55));

  print(fibonaci(10));

 final earth=Planet.earth;
 earth.describes();

//
}