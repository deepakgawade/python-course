abstract class Ingredient{
  late List<String> allergens;
  late String name;

  List<String> getAllergens() => allergens;
  String getName()=>name;
}


class BigBun extends Ingredient{
  BigBun(){allergens=['Wheat'];name='Big Mac Bun';}
}

class RegularBun extends Ingredient{
  RegularBun(){
    allergens=['Wheat'];
    name='Regular Bun';
  }
}

class BeefPatty extends Ingredient{

  BeefPatty(){
    allergens=[];
    name='Beef Patty';}

}

class McChickenPatty extends Ingredient{
  McChickenPatty(){
   allergens = [
      'Wheat',
      'Cooked in the same fryer that we use for Buttermilk Crispy Chicken which contains a milk allergen',
    ];
    name='McChicken Patty';
  }


  
}

class BigMacSauce extends Ingredient {
  BigMacSauce() {
    name = 'Big Mac Sauce';
    allergens = ['Egg', 'Soy', 'Wheat'];
  }
}

class Ketchup extends Ingredient {
  Ketchup() {
    name = 'Ketchup';
    allergens = [];
  }
}

class Mayonnaise extends Ingredient {
  Mayonnaise() {
    name = 'Mayonnaise';
    allergens = ['Egg'];
  }
}

class Mustard extends Ingredient {
  Mustard() {
    name = 'Mustard';
    allergens = [];
  }
}

class Onions extends Ingredient {
  Onions() {
    name = 'Onions';
    allergens = [];
  }
}

class PickleSlices extends Ingredient {
  PickleSlices() {
    name = 'Pickle Slices';
    allergens = [];
  }
}

class ShreddedLettuce extends Ingredient {
  ShreddedLettuce() {
    name = 'Shredded Lettuce';
    allergens = [];
  }
}

class Cheese extends Ingredient {
  Cheese() {
    name = 'Cheese';
    allergens = ['Milk', 'Soy'];
  }
}

class GrillSeasoning extends Ingredient {
  GrillSeasoning() {
    name = 'Grill Seasoning';
    allergens = [];
  }
}
