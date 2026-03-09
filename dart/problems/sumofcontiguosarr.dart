
///sliding window problem
void main(){

  List<int> arr = [7, 2, 3, 10, 5];
  int k = 3;
  int sum = 0;
  int maxSum=0;

  //O(n^2) solution

  // for(int i = 0; i < arr.length ; i++){

  //   for(int j = i; j < arr.length; j++){
  //     sum += arr[j];

  //     if(k==j-i+1){
  //     maxSum = maxSum > sum ? maxSum : sum;
  //       break;

  //     }

  //   }
  //   sum = 0;

  // }

  // print(maxSum);

//O(n) solution

  for(int i = 0; i < arr.length; i++){
    sum += arr[i];

    if (i >=k-1){
      maxSum = maxSum > sum ? maxSum : sum;
      sum -= arr[i-k+1]; //slding the window by removing the first element of the previous window
    }
  }



  print(maxSum);





}