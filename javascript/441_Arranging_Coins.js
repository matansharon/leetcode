// You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

// Given the integer n, return the number of complete rows of the staircase you will build.

 

// Example 1:


// Input: n = 5
// Output: 2
// Explanation: Because the 3rd row is incomplete, we return 2.
// Example 2:


// Input: n = 8
// Output: 3
// Explanation: Because the 4th row is incomplete, we return 3.
 

// Constraints:

// 1 <= n <= 231 - 1


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const arrangeCoins = (n) => {
  if (n === 1) {
    return 1;
  }
  let num_of_coins = n;
  let arr = [];
  let curr = 1;
  while (num_of_coins >= curr) {
    arr.push(curr);
    num_of_coins -= curr;
    curr++;
  }
  // console.log(arr.length);
  return arr.length;
};
//--------------------main----------------------------------------------------
arrangeCoins(5);
