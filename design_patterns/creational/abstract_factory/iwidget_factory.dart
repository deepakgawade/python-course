abstract interface class IWidgetFactory{

  String getTitle();

  IActivityIndicator createActivityIndicator();
  ISlider createSlider();
  ISwitch createSwitch();

}


class Widget{}

abstract interface class IActivityIndicator{
  Widget render();
} 

abstract interface class ISlider{
  Widget render();
}

abstract interface class ISwitch{
  Widget render();

}

class AndroidActivityIndicator implements IActivityIndicator{
  const AndroidActivityIndicator();
  
  @override
  render() {
    throw UnimplementedError();
  }


}


class AndroidSlider implements ISlider{
  const AndroidSlider();
  @override
  Widget render() {
    throw UnimplementedError();
  }
}

class AndroidSwitch implements ISwitch{

  const AndroidSwitch();
  @override
  Widget render() {
    throw UnimplementedError();
  }
  
}

class MaterialWidgetFactory implements IWidgetFactory{
  @override
  IActivityIndicator createActivityIndicator() {
   return const AndroidActivityIndicator();
  }

  @override
  ISlider createSlider() {
   return  const AndroidSlider();
  }

  @override
  ISwitch createSwitch() {
    return const AndroidSwitch();
  }

  @override
  String getTitle() {
    return 'Android';
  }
  
}
