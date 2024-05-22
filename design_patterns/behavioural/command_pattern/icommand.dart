abstract interface class Command{
  String getTitle();
  void execute();
  void undo();
}