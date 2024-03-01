import 'person.dart';

class Imposter implements Person{
  @override
  String greet(String other) {
    
   return "${other}, you know who I am";
   
  }
  
}

void main(){
  Person person=Person('Ram');
  Imposter imposter=Imposter();
  print( person.greet("Bharat"));
  print(imposter.greet("Bharat"));

}