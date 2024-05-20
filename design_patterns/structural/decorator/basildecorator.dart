import 'ipizza.dart';
import 'pizzadecorator.dart';

class Basil extends PizzaDecorator{
  Basil(super.pizza);

  @override
  String getDescription() {
  return '${pizza.getDescription()}\n - Basil';
  }

  @override
  double getPrice() {
return pizza.getPrice()+0.2;
  }

  
}