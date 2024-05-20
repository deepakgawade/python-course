import 'logbloc.dart';
import 'loglevel.dart';
import 'loglevelenum.dart';

class ExternalLoggingService{


  final LogBloc logBloc;

  ExternalLoggingService(this.logBloc);


  void logMessage(LogLevel logLevel, String message){
    final logMessage=LogMessage(logLevel: logLevel, message: message);

    logBloc.log(logMessage);
  }
  

}