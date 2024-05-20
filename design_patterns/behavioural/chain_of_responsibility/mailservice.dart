import 'logbloc.dart';
import 'loglevel.dart';
import 'loglevelenum.dart';

class MailService{

  final LogBloc logBloc;

  MailService(this.logBloc);


  void sendErrorMail(LogLevel logLevel,String message){

    final logMessage=LogMessage(logLevel: logLevel, message: message);

    logBloc.log(logMessage);

  }

}