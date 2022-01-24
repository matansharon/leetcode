// An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

// Given an integer n, return true if n is an ugly number.

 

// Example 1:

// Input: n = 6
// Output: true
// Explanation: 6 = 2 × 3
// Example 2:

// Input: n = 1
// Output: true
// Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
// Example 3:

// Input: n = 14
// Output: false
// Explanation: 14 is not ugly since it includes the prime factor 7.
 

// Constraints:

// -231 <= n <= 231 - 1


// this is a random generator for a binary tree in javascript

const randint = (val) => {
  return Math.floor(Math.random() * val);
};

const isUgly = (val) => {
  if (val <= 0) {
    return false;
  }
  while (val > 1) {
    if (val % 2 === 0) {
      val /= 2;
    } else if (val % 3 === 0) {
      val /= 3;
    } else if (val % 5 === 0) {
      val /= 5;
    } else {
      return false;
    }
  }
  return true;
};
//--------------------main----------------------------------------------------

