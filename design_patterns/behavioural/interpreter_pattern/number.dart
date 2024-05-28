import 'iexpression.dart';

class Number implements IExpression{

  final int number;
  Number(this.number);

  @override
  int interpret( context) => number;
  
}