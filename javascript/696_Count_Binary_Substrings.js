// Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

// Substrings that occur multiple times are counted the number of times they occur.

 

// Example 1:

// Input: s = "00110011"
// Output: 6
// Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
// Notice that some of these substrings repeat and are counted the number of times they occur.
// Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
// Example 2:

// Input: s = "10101"
// Output: 4
// Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
 

// Constraints:

// 1 <= s.length <= 105
// s[i] is either '0' or '1'.


const is_valid=(s)=>{
  let curr=s[0]
  let flag=false;
  let zero=0
  let one=0
  for(let i=0;i<s.length;i++){
    if(s[i]==='0'){zero++}
    else{one++;}
    if(s[i]!==curr){
      if(flag){return false;}
      else{
        flag=true;
        curr=s[i]
      }
    }
    
  }
  return zero===one;
}

const countBinarySubstrings=(s)=>{
  
  len=2;
  let res=0
  while(len<s.length){
    for(let i=0;i<s.length-len+1;i++){
      temp=s.slice(i,i+len);console.log(temp)
      if(is_valid(temp)){
        
        res++;}
    }
    len+=2;
  }
  // console.log(set)
  console.log(res)
  return res;
  
  
  
}
  //--------------------main----------------------------------------------------
countBinarySubstrings("00110011");
