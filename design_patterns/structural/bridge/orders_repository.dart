import 'enttity_base.dart';
import 'irepository.dart';
import 'istorage.dart';
import 'order.dart';

class OrdersRepository implements IRepository{

  const OrdersRepository(this.storage);

  final IStorage storage;
  @override
  List<EntityBase> getAll() {
  return storage.fetchAll<Order>();
  }

  @override
  void save(EntityBase entityBase) {
 storage.store(entityBase as Order);
  }
  
}