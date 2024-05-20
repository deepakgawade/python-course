import 'ipizza.dart';

class PizzaBase implements Pizza{

  final String description;

  PizzaBase( this.description);
  @override
  String getDescription() {
  return description;
  }

  @override
  double getPrice() {
return 3.0;
  }
  
}