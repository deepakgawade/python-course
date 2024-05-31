

//times=[1,3,1,4,8]
//trees=[5,1,2,7]
//persons=[2,1]

void main(){
  var times=[1,2,1];//16

  print(getTotalTime(times));

}

int getTotalTime( List<int> times){
   int sum=0;
  // int totalTime=0;
  for(int i=0;i<times.length;i++){
 

      for(int j=0;j<=i;j++){

        sum=sum+times[j];
      }

      // totalTime=totalTime+sum;

  }
  return sum;
}