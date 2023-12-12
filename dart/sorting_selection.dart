void main() {

  List<int> elements=[19,54,86,10,8,43];
 elements.forEach(print);
  for(int i=0;i<elements.length-2;i++){

    int minimum=i;

    for (int j=i;j<elements.length-1;j++){

      if (elements[j]<elements[minimum]){
        minimum=j;

      }
      


    }
      int  temp=0;

    temp=elements[i];
    elements[i]=elements[minimum];
    elements[minimum]=temp;


  }
  elements.forEach(print);

  
}
  swap(int i, int j){
  int  temp=0;

    temp=i;
    i=j;
    j=temp;

  }

