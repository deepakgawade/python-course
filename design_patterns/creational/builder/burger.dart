import 'ingredient.dart';

class Burger {
  final List<Ingredient> _ingredients=[];

  late double _price;

  void addIngredient(Ingredient ingredient){
    _ingredients.add(ingredient);
  }

  void setPrice(double value){
    _price=value;
  }

  String getFormattedIngredients()=> _ingredients.map((e) => e.getName()).join(',');

  String getFormattedAllergens()=><String>{for( final x in _ingredients) ...x.getAllergens() }.join(',');

  String getFormattedPrice() => '\$${_price.toStringAsFixed(2)}';

}