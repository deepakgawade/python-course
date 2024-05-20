import 'ipizza.dart';

 abstract class PizzaDecorator implements Pizza{

  final Pizza pizza;

  PizzaDecorator(this.pizza);

  @override
  String getDescription() {
  return pizza.getDescription();
  }
 
  @override
  double getPrice() {
 return pizza.getPrice();
  }

}