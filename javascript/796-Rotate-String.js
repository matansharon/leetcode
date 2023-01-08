// Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

// A shift on s consists of moving the leftmost character of s to the rightmost position.

// For example, if s = "abcde", then it will be "bcdea" after one shift.
 

// Example 1:

// Input: s = "abcde", goal = "cdeab"
// Output: true
// Example 2:

// Input: s = "abcde", goal = "abced"
// Output: false
 

// Constraints:

// 1 <= s.length, goal.length <= 100
// s and goal consist of lowercase English letters


const randint=(max)=>{
  return Math.floor(Math.random()*max)
}
const gen_arr=()=>{
  let res=[]
  let len=randint(50)+1
  for(let i=0;i<len;i++){
    res.push(randint(100))
  }
  return res;
}
const rotateString=(s,goal)=>{
  let temp=''
  temp=s+s
  return s.length===goal.length && (s+s).includes(goal)
}
  //--------------------main----------------------------------------------------
console.log(rotateString("abcde","cdeab"))
