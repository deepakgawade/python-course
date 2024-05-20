import 'dart:async';
import 'dart:collection';

import 'loglevel.dart';

class LogBloc{
  final List<LogMessage> _logs=[];


  final _logStream= StreamController<List<LogMessage>>();

  StreamSink <List<LogMessage>> get inLogStream=>_logStream.sink;
  Stream<List<LogMessage>> get outLogStream=>_logStream.stream;

  void log(LogMessage logMessage){
    _logs.add(logMessage);
    inLogStream.add(UnmodifiableListView(_logs));
  }

  void dispose(){
    _logStream.close();
  }

}