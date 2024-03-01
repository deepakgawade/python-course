

Stream<String> getItems(Iterable<int> elements) async*{

  for(final item in elements){
    await Future.delayed(Duration(seconds: 1));

    yield 'part ${item}';

  }

}


extension DateString on DateTime {
  String parseDate(){
  

    
    return 'Todays Month ${this.month}';
  }
}

void main(){
  Iterable<int> list=[1,2,3,4,5,6,7,8,9,10];

 // getItems(list).forEach((element) {print(element);});

DateTime tume= DateTime.now();
print(tume.parseDate());


}

