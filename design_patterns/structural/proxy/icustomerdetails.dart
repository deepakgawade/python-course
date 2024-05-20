import 'cunstomerdetail.dart';

abstract interface class ICustomerDetailsService{
  Future<CustomerDetails> getCustomerDetails(String id);
}