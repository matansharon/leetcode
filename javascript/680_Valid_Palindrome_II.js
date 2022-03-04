// Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

// Example 1:

// Input: s = "aba"
// Output: true
// Example 2:

// Input: s = "abca"
// Output: true
// Explanation: You could delete the character 'c'.
// Example 3:

// Input: s = "abc"
// Output: false
 

// Constraints:

// 1 <= s.length <= 105
// s consists of lowercase English letters.


const is_palindrom=(s)=>{
  let start=0;
  let end=s.length-1;
  // console.log(start,end);
  while(start<end){
    if(s[start]!==s[end]){return false;}
    start++;
    end--;

  }
  return true
}
const validPalindrome=(s)=>{
  let arr=[]
    for(let i=1;i<s.length+1;i++){
      let temp=s.slice(0,i-1)+s.slice(i,s.length);
      if(is_palindrom(temp)){return true;}
      
      
  }
  return false;
  
}
  //--------------------main----------------------------------------------------
console.log(validPalindrome("aabba"));
