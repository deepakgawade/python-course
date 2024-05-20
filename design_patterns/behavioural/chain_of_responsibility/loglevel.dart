import '../../structural/composite/ifile.dart';
import 'loglevelenum.dart';

class LogMessage{
  


  final LogLevel logLevel;
  final String message;

  LogMessage({required this.logLevel, required this.message});


  String get _logLevelString=>logLevel.toString().split('.').last.toUpperCase();

  Color _getLogEntryColor()=>switch(logLevel){

    LogLevel.debug=>Color.grey,
    LogLevel.error=>Color.blue,
    LogLevel.info=>Color.red,

  };

    Widget getFormattedMessage() => Text(
        '$_logLevelString: $message',
        style: TextStyle(color: _getLogEntryColor()),
        textAlign: TextAlign.justify,
        overflow: TextOverflow.ellipsis,
        maxLines: 2,
      );


}
class Color{

}

