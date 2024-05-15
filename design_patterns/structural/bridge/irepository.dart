import 'enttity_base.dart';

abstract interface class IRepository{

List<EntityBase> getAll();
void save(EntityBase entityBase);
}