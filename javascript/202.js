// Write an algorithm to determine if a number n is happy.

// A happy number is a number defined by the following process:

// Starting with any positive integer, replace the number by the sum of the squares of its digits.
// Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
// Those numbers for which this process ends in 1 are happy.
// Return true if n is a happy number, and false if not.

 

// Example 1:

// Input: n = 19
// Output: true
// Explanation:
// 12 + 92 = 82
// 82 + 22 = 68
// 62 + 82 = 100
// 12 + 02 + 02 = 1
// Example 2:

// Input: n = 2
// Output: false
 

// Constraints:

// 1 <= n <= 231 - 1


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const isHappy = (n) => {
  let map = new Map();
  let num = n;

  while (true) {
    if (sum_digits(num) === 1) {
      return true;
    } else {
      map.set(num);
      num = sum_digits(num);
    }
    if (map.has(num)) {
      return false;
    }
  }
};
const sum_digits = (_num) => {
  let res = 0;
  let num = _num.toString();
  for (let i = 0; i < num.length; i++) {
    res += Math.pow(Number.parseInt(num[i]), 2);
  }
  return res;
};
//--------------------main----------------------------------------------------
let max = Math.pow(2, 32) - 1;
let target = randint(max);
console.log(target, isHappy(target));
