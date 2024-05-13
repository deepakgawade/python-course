import 'singleton.dart';

final class ExampleStateDefination extends ExampleStateBase{

  static ExampleStateDefination? _instance; 


  ExampleStateDefination._internal(){
    initialText='A new \'ExampleStateByDefinition\' instance has been created.';
    stateText=initialText;
  }

  static ExampleStateDefination getState(){
    return _instance??=ExampleStateDefination._internal();
  }


}


final class  ExampleState extends ExampleStateBase{
  
  static final ExampleState instance= ExampleState._internal();

  factory ExampleState(){
   return instance; 
  }

  ExampleState._internal(){
    initialText='A new \'ExampleState\' instance has been created.';

    stateText=initialText;
  }
}


