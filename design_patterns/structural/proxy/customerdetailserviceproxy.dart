import 'cunstomerdetail.dart';
import 'icustomerdetails.dart';

class CustomerDetailsServiceProxy implements ICustomerDetailsService{
  CustomerDetailsServiceProxy(this.service);

  final ICustomerDetailsService service;
  final Map<String,CustomerDetails> customerDetailCache={}; 

  @override
  Future<CustomerDetails> getCustomerDetails(String id) async {

    if (customerDetailCache.containsKey(id)) return customerDetailCache[id]!;


    final customerDetails=await service.getCustomerDetails(id);

        customerDetailCache[id] = customerDetails;

        return customerDetails;


  }
  
}