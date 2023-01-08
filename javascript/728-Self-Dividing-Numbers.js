// A self-dividing number is a number that is divisible by every digit it contains.

// For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
// A self-dividing number is not allowed to contain the digit zero.

// Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

 

// Example 1:

// Input: left = 1, right = 22
// Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
// Example 2:

// Input: left = 47, right = 85
// Output: [48,55,66,77]
 

// Constraints:

// 1 <= left <= right <= 104


const is_dvise=(num)=>{
  s=num.toString();
  for(let i=0;i<s.length;i++){
    if(s[i]==='0'){return false;}
    if(num%parseInt(s[i])!==0){return false;}
  }
  return true;
}
const selfDividingNumbers=(left,right)=>{
  let res=[]
  for(let i=left;i<right+1;i++){
    if(is_dvise(i)){res.push(i)}
  }
  return res;
}
  //--------------------main----------------------------------------------------
console.log(is_dvise(16))
