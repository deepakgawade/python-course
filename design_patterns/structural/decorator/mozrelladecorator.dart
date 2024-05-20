import 'pizzadecorator.dart';

class Mozzarella extends PizzaDecorator {
   Mozzarella(super.pizza);

  @override
  String getDescription() => '${pizza.getDescription()}\n- Mozzarella';

  @override
  double getPrice() => pizza.getPrice() + 0.5;
}