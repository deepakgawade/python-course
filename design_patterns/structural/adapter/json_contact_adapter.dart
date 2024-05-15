import 'dart:convert';

import 'contact.dart';
import 'icontact.dart';
import 'jsoncontactapi.dart';

class JsonContactAdapter implements IContactsAdapter{

  final JsonContactApi api;

   JsonContactAdapter({this.api=const JsonContactApi()});
  @override
  List<Contact> getContacts() {

    final contactsjson=api.getContactJson();
    final contactlist=_parsedjson(contactsjson);


return [];


  }


  List<Contact> _parsedjson(String contactJson){

        final contactsMap = json.decode(contactJson) as Map<String, dynamic>;
    final contactsJsonList = contactsMap['contacts'] as List;
    final contactsList = contactsJsonList.map((json) {
      final contactJson = json as Map<String, dynamic>;

      return Contact(
        fullName: contactJson['fullName'] as String,
        email: contactJson['email'] as String,
        favorite: contactJson['favourite'] as bool,
      );
    }).toList();

    return contactsList;
  }
}