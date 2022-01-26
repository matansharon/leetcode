// Given an integer n, return true if it is a power of three. Otherwise, return false.

// An integer n is a power of three, if there exists an integer x such that n == 3x.

 

// Example 1:

// Input: n = 27
// Output: true
// Example 2:

// Input: n = 0
// Output: false
// Example 3:

// Input: n = 9
// Output: true
 

// Constraints:

// -231 <= n <= 231 - 1
 

// Follow up: Could you solve it without loops/recursion?


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const canWinNim = (n) => {
  if (n < 4) {
    return true;
  }
};
const isPowerOfThree = (n) => {
  if (n < 0) {
    return false;
  }
  let pow = 0;

  for (let i = 0; i < 20; i++) {
    if (3 ** i === n) {
      return true;
    }
  }
  return false;
};
//--------------------main----------------------------------------------------
