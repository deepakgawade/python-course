class Person{
  final String _name;

  Person(this._name);

  String greet(String other){
    return 'Hi ${other}, I am ${this._name}';
  }

}