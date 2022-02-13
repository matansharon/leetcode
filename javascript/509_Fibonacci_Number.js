// The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

// F(0) = 0, F(1) = 1
// F(n) = F(n - 1) + F(n - 2), for n > 1.
// Given n, calculate F(n).

 

// Example 1:

// Input: n = 2
// Output: 1
// Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
// Example 2:

// Input: n = 3
// Output: 2
// Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
// Example 3:

// Input: n = 4
// Output: 3
// Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

// Constraints:

// 0 <= n <= 30


const randint = (val) => {
    return Math.floor(Math.random() * val);
}
const fib=(n)=>{
    if(n===0){return 0}
    let arr=[1,1]
    if(n<3){return arr[n]}
    for(let i=2;i<n;i++){
        let len=arr.length
        arr.push(arr[len-1]+arr[len-2])
    }
    console.log(arr[arr.length-1])
    return arr[arr.length-1]
}
  //--------------------main----------------------------------------------------
for(let i=0;i<20;i++){
    fib(i)
}
