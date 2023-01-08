// Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

// Example 1:

// Input: nums = [3,0,1]
// Output: 2
// Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
// Example 2:

// Input: nums = [0,1]
// Output: 2
// Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
// Example 3:

// Input: nums = [9,6,4,2,3,5,7,0,1]
// Output: 8
// Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

// Constraints:

// n == nums.length
// 1 <= n <= 104
// 0 <= nums[i] <= n
// All the numbers of nums are unique.


// this is a random generator for a binary tree in javascript
// var _ = require("underscore");
const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_array = () => {
  let len = randint(100);
  let arr = [];
  for (let i = 0; i < len; i++) {
    arr.push(i);
  }
  arr.sort(() => 0.5 - Math.random());
  return arr;
};
const missingNumber = (arr) => {
  arr.sort((a, b) => {
    return a - b;
  });
  // console.log(arr);
  if (arr[0] !== 0) {
    return 0;
  }
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i + 1] - arr[i] !== 1) {
      return arr[i] + 1;
    }
  }
  return arr[arr.length - 1] + 1;
};
//--------------------main----------------------------------------------------
let arr = random_array();
arr.pop();
console.log(missingNumber(arr));
