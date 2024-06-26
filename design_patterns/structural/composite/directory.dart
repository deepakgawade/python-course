
import 'ifile.dart';

class Directory extends StatelessWidget implements IFile{

  final String title;
  final List<IFile> files=[];
  final bool isInitiallyExpanded;

  Directory( this.title,{ this.isInitiallyExpanded=false});


void addFile(IFile file)=>files.add(file);
  
  @override
  int getSize() {

    int sum=0;
  for(final file in files){
    sum=sum+file.getSize();
  }
  return sum;
  }

    @override
  Widget render(BuildContext context) {
    return Theme(
      data: ThemeData(
        expansionTileTheme: Theme.of(context)
            .expansionTileTheme
            .copyWith(iconColor: Colors.black, textColor: Colors.black),
      ),
      child: Padding(
        padding: const EdgeInsets.only(left: LayoutConstants.paddingS),
        child: ExpansionTile(
          leading: const Icon(Icons.folder),
          title: Text('$title (${FileSizeConverter.bytesToString(getSize())})'),
          initiallyExpanded: isInitiallyExpanded,
          children: files.map((IFile file) => file.render(context)).toList(),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) => render(context);

  
  
}
