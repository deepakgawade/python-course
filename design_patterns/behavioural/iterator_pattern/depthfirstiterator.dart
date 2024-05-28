import 'dart:collection';

import 'depthfirsttreecollection.dart';
import 'iiterator.dart';

class DepthFirstIterator implements ITreeIterator{

  final DepthFirstTreeCollection treeCollection;
  final Set<int> visitedNodes=<int>{};
  final ListQueue<int> nodeStack=ListQueue<int>();

  final initialNode=1;
  late int _currenytNode;
  DepthFirstIterator(this.treeCollection){
    _currenytNode=initialNode;
  }

  @override
  int? getNext() {
    // TODO: implement getNext
    throw UnimplementedError();
  }

  @override
  bool hasNext() {
    // TODO: implement hasNext
    throw UnimplementedError();
  }

  @override
  void reset() {
    // TODO: implement reset
  }
  
}