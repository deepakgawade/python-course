import 'cunstomerdetail.dart';
import 'icustomerdetails.dart';

class CustomerDetailsService implements ICustomerDetailsService{
  @override
  Future<CustomerDetails> getCustomerDetails(String id) =>Future.delayed(Duration(seconds: 2),()=>CustomerDetails(customerId: '123456', email: 'kjadsjk@gmail.com', hobby: 'pds', position: 'jdjfj'));

}