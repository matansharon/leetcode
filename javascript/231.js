// Given an integer n, return true if it is a power of two. Otherwise, return false.

// An integer n is a power of two, if there exists an integer x such that n == 2x.

 

// Example 1:

// Input: n = 1
// Output: true
// Explanation: 20 = 1
// Example 2:

// Input: n = 16
// Output: true
// Explanation: 24 = 16
// Example 3:

// Input: n = 3
// Output: false
 

// Constraints:

// -231 <= n <= 231 - 1
 

// Follow up: Could you solve it without loops/recursion?


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const isPowerOfTwo = (n) => {
  if (n < 1) {
    return false;
  }
  let map = new Map();
  let curr = 0;
  res = Math.pow(2, curr);
  while (res < Math.pow(2, 31) - 1) {
    map.set(res);
    curr++;
    res = Math.pow(2, curr);
  }
  return map.has(n);
};

//second soltuion
const isPowerOfTwo = (n) => {
  if (n < 1) {
    return false;
  }
  let x = n;
  return (x & -x) === x;
};
//--------------------main----------------------------------------------------
console.log(isPowerOfTwo(4));
