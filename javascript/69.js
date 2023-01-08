// Given a non-negative integer x, compute and return the square root of x.

// Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

// Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

// Example 1:

// Input: x = 4
// Output: 2
// Example 2:

// Input: x = 8
// Output: 2
// Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

// Constraints:

// 0 <= x <= 231 - 1


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const mySqrt = function (x) {
  if (x < 2) {
    return x;
  }
  let res = -1;
  for (let i = 2; i < Math.sqrt(Math.pow(2, 31)); i++) {
    if (i * i > target) {
      res = i;
      console.log(i);
      break;
    }
  }
  return res - 1;
};
//--------------------main----------------------------------------------------

let target = randint(10000000);
console.log(target);
console.log(Math.sqrt(target));
mySqrt(target);
// console.log(Math.sqrt(Math.pow(2, 31)));
