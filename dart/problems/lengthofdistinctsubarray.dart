void main(){
  String str = "abcabcdebb";
  int maxLength = 0;
 
//O(n^2) solution

//   for(int i=0; i<str.length; i++){
//  Set<String> seen = {};


//     for(int j=i;j<str.length; j++){

//       if(seen.contains(str[j])){
//         break;
//       }

//       seen.add(str[j]);
//       maxLength = maxLength > j-i+1 ? maxLength : j-i+1;

//     }
   
//   }

  ///O(n) solution

  int i=0;
  Map<String, int> seen = {};
  for(int j=0; j<str.length;j++){
    String char =str[j];
    if (seen.containsKey(char)){
      i = seen[char]!+1;//slide the window to the right of the last occurrence of the character
    }
    seen[char] =j;//update the last occurrence of the character in map
    maxLength=maxLength >j-i+1?maxLength:j-i+1;
  }

  print(maxLength);
}