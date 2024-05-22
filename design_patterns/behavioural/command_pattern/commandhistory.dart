import 'dart:collection';

import 'icommand.dart';

class CommandHistory{

  final _commandList=ListQueue<Command>();


bool get isEmpty=> _commandList.isEmpty;

List<String> get commandList => _commandList.map((element) => element.getTitle()).toList();

void undo(){
  if(_commandList.isEmpty)return;

  _commandList.removeLast().undo();
}
}