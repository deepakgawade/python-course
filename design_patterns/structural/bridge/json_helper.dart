import 'dart:convert';

import 'customer.dart';
import 'enttity_base.dart';
import 'order.dart';

class JsonHelper{
  static String serialiseObject(EntityBase entityBase){
    return jsonEncode(entityBase);
  }

//restricting the return types generics
static T desetialiseObject<T extends EntityBase>(String jsonstring){

  final json=jsonDecode(jsonstring) as Map<String, dynamic>;

  return switch(T){
    const (Customer)=>Customer.fromJson(json) as T,
    const (Order)=>Order.fromJson(json) as T,
    _=>throw Exception("Type of '$T' is not supported."),

  };

}
}