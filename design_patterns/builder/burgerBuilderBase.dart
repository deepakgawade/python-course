import 'burger.dart';
import 'ingredient.dart';

abstract class BurgerBuilderBase{

  late Burger burger;
  late double price;


  createBurger(){
    return burger=Burger();
  }

  Burger getBurger()=>burger;

  void setBurgerPrice(){
    burger.setPrice(price);
  }

  void addBuns();
  void addCheese();
  void addPatties();
  void addSauces();
  void addSeasoning();
  void addVegetables();
}

class BigMacBuilder extends BurgerBuilderBase{
  BigMacBuilder(){
    price=3.99;

  }
   @override
  void addBuns() {
    burger.addIngredient(BigBun());
  }

  @override
  void addCheese() {
    burger.addIngredient(Cheese());
  }

  @override
  void addPatties() {
    burger.addIngredient(BeefPatty());
  }


  @override
  void addVegetables() {
    burger.addIngredient(Onions());
    burger.addIngredient(PickleSlices());
    burger.addIngredient(ShreddedLettuce());
  }
  
   @override
  void addSauces() {
    burger.addIngredient(BigMacSauce());
  }

  @override
  void addSeasoning() {
    burger.addIngredient(GrillSeasoning());
  }

}

class HamburgerBuilder extends BurgerBuilderBase {
  HamburgerBuilder() {
    price = 1.0;
  }

  @override
  void addBuns() {
    burger.addIngredient(RegularBun());
  }

  @override
  void addCheese() {
    // Not needed
  }

  @override
  void addPatties() {
    burger.addIngredient(BeefPatty());
  }

  @override
  void addSauces() {
    burger.addIngredient(Ketchup());
    burger.addIngredient(Mustard());
  }
  
  @override
  void addSeasoning() {
    // TODO: implement addSeasoning
  }
  
  @override
  void addVegetables() {
    // TODO: implement addVegetables
  }

}