import 'enttity_base.dart';

class Customer extends EntityBase{
  final String name;
  final String email;


  Customer():email=faker.person.email,name=faker.person.name;

  Customer.fromJson(super.json):email=json['name'] as String,name=json['email'] as String,super.fromJson(json);
  Map<String, dynamic> toJson(){
    return {
      'id':id,
      'name':name,
      'email':email
    };
  }


}