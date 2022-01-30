// Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

// Example 1:

// Input: nums = [4,3,2,7,8,2,3,1]
// Output: [5,6]
// Example 2:

// Input: nums = [1,1]
// Output: [2]
 

// Constraints:

// n == nums.length
// 1 <= n <= 105
// 1 <= nums[i] <= n
 

// Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_arr = () => {
  let len = 20;
  let res = [];
  for (let i = 1; i < len; i++) {
    if (Math.random() < 0.7) {
      res.push(i);
    } else {
      res.push(res[randint(res.length)]);
    }
  }
  return res;
};
const findDisappearedNumbers = (nums) => {
  let map = new Map();
  for (let i = 1; i < nums.length + 1; i++) {
    map.set(i, 0);
  }
  nums.forEach((v) => {
    map.set(v, map.get(v) + 1);
  });
  let res = [];
  for ([key, value] of map) {
    if (value === 0) {
      res.push(key);
    }
  }
  console.log(res);
  return res;
};
//--------------------main----------------------------------------------------
let arr = random_arr();
console.log(arr.length);
findDisappearedNumbers(arr);
