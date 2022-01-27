// Given a positive integer num, write a function which returns True if num is a perfect square else False.

// Follow up: Do not use any built-in library function such as sqrt.

 

// Example 1:

// Input: num = 16
// Output: true
// Example 2:

// Input: num = 14
// Output: false
 

// Constraints:

// 1 <= num <= 2^31 - 1

const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const isPerfectSquare = (num) => {
  for (let i = 0; i ** 2 < Math.pow(2, 31) - 1; i++) {
    if (i ** 2 === num) {
      return true;
    }
    // console.log(i**2)
  }
  return false;
};
//--------------------main----------------------------------------------------
isPerfectSquare(randint(Math.pow(2,31)-1));
