
import 'burger.dart';
import 'burgerBuilderBase.dart';

class BurgerMaker{
  BurgerMaker(this.burgerBuilder);
  BurgerBuilderBase burgerBuilder;

  void changeBurgerBuilder(BurgerBuilderBase burgerbuilder1){

    this.burgerBuilder=burgerbuilder1;

  }

  Burger getBurger()=>burgerBuilder.getBurger();


  void prepareBurger() {
    burgerBuilder.createBurger();
    burgerBuilder.setBurgerPrice();

    burgerBuilder.addBuns();
    burgerBuilder.addCheese();
    burgerBuilder.addPatties();
    burgerBuilder.addSauces();
    burgerBuilder.addSeasoning();
    burgerBuilder.addVegetables();
  }

  
}