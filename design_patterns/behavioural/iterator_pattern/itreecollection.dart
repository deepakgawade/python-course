import 'iiterator.dart';

abstract interface class ITreeCollection{
  ITreeIterator createIterator();
  String getTitle();
}