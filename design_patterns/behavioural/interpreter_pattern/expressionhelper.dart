import 'dart:collection';
import 'dart:html';

import 'add.dart';
import 'iexpression.dart';
import 'multiply.dart';
import 'number.dart';
import 'subtract.dart';

class ExpressionHelper{

  const ExpressionHelper._();
  static final List<String> _operators=['*','+','-'];

  static IExpression buildExpressionTree(String postfixExparession){
    final expressionStack=ListQueue<IExpression>();

    for(final symbol in postfixExparession.split(' ')){

      if(isOperator(symbol)){

        final right=expressionStack.removeLast();
        final left=expressionStack.removeLast();
        final nonterminalexpression= _getNonTerminalExpression(symbol, right, left);

        expressionStack.addLast(nonterminalexpression);

      }
      else{

        final  numberExpression= Number(int.parse(symbol));

        expressionStack.addLast(numberExpression);
      }

    }
    return expressionStack.single;

  }

  static bool isOperator(String symbol){

   return _operators.contains(symbol);

  }

  static IExpression _getNonTerminalExpression(String operator,IExpression right,IExpression left){
    return switch(operator){
      '+'=> Add(left, right),
      '-'=>Subtract(left, right),
      '*'=>Multiply(left, right),
      _=>throw Exception('Expression is not defined')
    };
  }

}