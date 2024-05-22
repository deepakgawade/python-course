import 'icommand.dart';
import 'shape.dart';

class ChangeHeightCommand implements Command{

  final Shape shape;
  final double previousHeight;

  ChangeHeightCommand(this.shape):previousHeight=shape.height;

  @override
  void execute()=> shape.height = random.integer(150, min: 50).toDouble();

  @override
  String getTitle() {
return 'Change Height';
  }

  @override
  void undo() {
 shape.height=previousHeight;
  }
  
}