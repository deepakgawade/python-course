import 'customer.dart';
import 'enttity_base.dart';
import 'irepository.dart';
import 'istorage.dart';

class CustomerRepository implements IRepository{

  const CustomerRepository(this.storage);

  final IStorage storage;
  @override
  List<EntityBase> getAll() {
    return storage.fetchAll<Customer>();
  }

  @override
  void save(EntityBase entityBase) {
    storage.store(entityBase as Customer);
  }
  
}