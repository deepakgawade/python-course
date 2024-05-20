
abstract interface class IFile{
  int getSize();
  Widget render(BuildContext context);
}

sealed class Widget{}
sealed class BuildContext {}