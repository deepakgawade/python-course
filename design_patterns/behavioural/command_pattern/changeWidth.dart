import 'icommand.dart';
import 'shape.dart';

class ChangeWidthCommand implements Command{
  final Shape shape;
  final double prevoiusWidth;

  ChangeWidthCommand(this.shape):prevoiusWidth=shape.width;
  
  @override
  void execute() =>shape.width = random.integer(150, min: 50).toDouble();
  
  @override
  String getTitle() {
    return 'Change Width';
  }
  
  @override
  void undo() =>shape.width=prevoiusWidth;

  
}