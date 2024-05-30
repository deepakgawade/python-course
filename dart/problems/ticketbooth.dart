

//times=[1,3,1,4,8]
//

void main(){
  var times=[1,2,1,4];//10

  print(getTotalTime(times));

}

int getTotalTime( List<int> times){

  int totalTime=0;
  for(int i=0;i<times.length;i++){
    int sum=0;

      for(int j=0;j<=i;j++){

        sum=sum+times[j];
      }

      totalTime=totalTime+sum;

  }
  return totalTime;
}