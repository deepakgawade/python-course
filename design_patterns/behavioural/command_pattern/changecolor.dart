import 'icommand.dart';
import 'shape.dart';

class ChangeColorCommand implements Command{

  final Shape shape;
  final Color previousColor;
  ChangeColorCommand(this.shape):previousColor=shape.color;

  @override
  void execute() => shape.color = Color.fromRGBO(
        random.integer(255),
        random.integer(255),
        random.integer(255),
        1.0,
      );

  @override
  String getTitle() {
  return 'Change color';
  }

  @override
  void undo() => shape.color = previousColor;

}