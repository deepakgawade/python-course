import 'enttity_base.dart';
import 'istorage.dart';
import 'json_helper.dart';

class FileStorage implements IStorage{

  final Map<Type,List<String>> filestorage={};
  @override
  List<T> fetchAll<T extends EntityBase>() {

    if(!filestorage.containsKey(T))return [];

    final files=filestorage[T];
    return files!.map<T>((e) => JsonHelper.desetialiseObject<T>(e)).toList();

  }

  @override
  String getTitle() {
   return 'File Storage';
  }

  @override
  void store<T extends EntityBase>(T entityBase) {
 if (!filestorage.containsKey(T))filestorage[T]=[];
 filestorage[T]!.add(JsonHelper.serialiseObject(entityBase));
  }
  
}