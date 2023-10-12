class SmartDevice ( val name: String, val category: String) {


    var deviceStatus = "online"

    fun turnOn(){
        println("Smart Device is turned on")
    }

    fun turnOff(){
        println("Smart Device is turned off")
    }


}