// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

// A subarray is a contiguous part of an array.

 

// Example 1:

// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.
// Example 2:

// Input: nums = [1]
// Output: 1
// Example 3:

// Input: nums = [5,4,-1,7,8]
// Output: 23
 

// Constraints:

// 1 <= nums.length <= 105
// -104 <= nums[i] <= 104
 

// Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

const random_array = function () {
  let arr = [];
  let len = Math.floor(Math.random() * 100);
  len = 5;

  for (let i = 0; i < len; i++) {
    let temp = Math.floor(Math.random() * 100);
    let pos_neg = Math.random();
    // console.log(pos_neg);
    if (pos_neg < 0.5) {
      temp *= -1;
    }
    arr.push(temp);
  }
  return arr;
};
const liniar_search = function (arr, val) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === val) {
      return i;
    }
  }
  return -1;
};
const all_sub_arr = function (arr) {
  let res = Number.MIN_VALUE;
  for (let len = 1; len <= arr.length; len++) {
    for (let start = 0; start < arr.length - len + 1; start++) {
      let temp = arr.slice(start, start + len).reduce(add, 0);
      console.log(temp);
      if (temp > res) {
        res = temp;
      }
    }
  }
  return res;
};
const add = function (acc, a) {
  return acc + a;
};
// //-----------------------------------------main----------------------------------------------
arr = random_array();
console.log(arr);

let res = all_sub_arr(arr);
console.log(res);
