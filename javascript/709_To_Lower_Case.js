// Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

// Example 1:

// Input: s = "Hello"
// Output: "hello"
// Example 2:

// Input: s = "here"
// Output: "here"
// Example 3:

// Input: s = "LOVELY"
// Output: "lovely"
 

// Constraints:

// 1 <= s.length <= 100
// s consists of printable ASCII characters.


const randint=(val)=>{
  return Math.floor(Math.random()*val)
}

const toLowerCase=(s)=>{
  
  let upper_low=new Map();
  let res=''
  let ab="abcdefghijklmnopqrstuvwxyz"
  let AB="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for(let i=0;i<ab.length;i++){
    
    upper_low.set(AB[i],ab[i])
  }
  // console.log(upper_low)
  for(let i=0;i<s.length;i++){
    if(upper_low.has(s[i])){res+=upper_low.get(s[i])}
    else{res+=s[i]}
  }
  return res;
}

  //--------------------main----------------------------------------------------

toLowerCase("AaaBMJYaaa")
