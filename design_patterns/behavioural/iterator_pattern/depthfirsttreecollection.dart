import 'graph.dart';
import 'iiterator.dart';
import 'itreecollection.dart';

class DepthFirstTreeCollection implements ITreeCollection{

  DepthFirstTreeCollection(this.graph);

  final Graph graph;
  @override
  ITreeIterator createIterator() {
    // TODO: implement createIterator
    throw UnimplementedError();
  }

  @override
  String getTitle() {
    // TODO: implement getTitle
    throw UnimplementedError();
  }
}