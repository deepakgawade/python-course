
merge_sort(List<int> arr, int low, int high){
  if(low==high) return;

  int mid= ((low+high)/2).floor();

  merge_sort(arr, low, mid);
  merge_sort(arr, mid+1, high);
  merge(arr, low,mid , high);

}

merge(List<int> arr, int low, int mid, int high){
  List<int > temp=[];

  int left= low;
  int right= mid+1;
  print(arr);

  while(left<=mid&&right<=high){
    if(arr[left]<arr[right]){
      temp.add(arr[left]);
      left+=1;

    }else{
      temp.add(arr[right]);
      right+=1;
    }
  }

  while(left<=mid){
    temp.add(arr[left]);
      left+=1;
  }
  while(right<=high){
    temp.add(arr[right]);
      right+=1;
  }
    print(temp);

  for(int i=low; i<=high;i++)
  {
    arr[i]=temp[i-low];
    print("i : ${i}, high: ${high}, low:${low}");
  }

}
void main(){
  List<int> elemts=[19,54,86,10,8,43];
  List<int> elemts2=[5,4,3,2,1,0];
  merge_sort(elemts2,0, elemts2.length-1);
  print(elemts2);
}