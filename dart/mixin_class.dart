mixin Musical{
  void play(){
    print("playing guitar");
  }
}

mixin Rider{
    void ride(){
    print("riding in car");
  }
}

class Person {
  final String parameterName;
  Person(this.parameterName);
  void player(){
    print("I am ${this.parameterName}");
  }

}

class Maestro extends Person with Musical, Rider {

    Maestro(parameterName):super(parameterName);

}


abstract mixin class Music{
  void playIntrumemts();

  void sing(){
    print("singing a song");
  }
}

class Vituasa with Music{
  @override
  void playIntrumemts() {
    // TODO: implement playIntrumemts
  }

}


class Magnum extends Music{
  @override
  void playIntrumemts() {
    // TODO: implement playIntrumemts
  }

}

void main(){
  Maestro mesto=Maestro("Ram");

  mesto.play();
  mesto.player();
  mesto.ride();
}



