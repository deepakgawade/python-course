import 'enttity_base.dart';


class Order extends EntityBase{

  Order(): dishes=List.generate(random.integer(3, min: 1), (_) => faker.food.dish()),total=random.decimal(3, min: 1);

  final List<String> dishes;
  final double total;

  Order.fromJson(super.json)
      : dishes = List.from(json['dishes'] as List),
        total = json['total'] as double,
        super.fromJson();

  Map<String, dynamic> toJson() => {
        'id': id,
        'dishes': dishes,
        'total': total,
      };

}