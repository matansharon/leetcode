// Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

// Example 1:

// Input: nums = [3,2,1]
// Output: 1
// Explanation:
// The first distinct maximum is 3.
// The second distinct maximum is 2.
// The third distinct maximum is 1.
// Example 2:

// Input: nums = [1,2]
// Output: 2
// Explanation:
// The first distinct maximum is 2.
// The second distinct maximum is 1.
// The third distinct maximum does not exist, so the maximum (2) is returned instead.
// Example 3:

// Input: nums = [2,2,3,1]
// Output: 1
// Explanation:
// The first distinct maximum is 3.
// The second distinct maximum is 2 (both 2's are counted together since they have the same value).
// The third distinct maximum is 1.
 

// Constraints:

// 1 <= nums.length <= 104
// -231 <= nums[i] <= 231 - 1
 

// Follow up: Can you find an O(n) solution?


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_array = () => {
  let len = randint(100);
  let arr = [];
  for (let i = 0; i < len; i++) {
    arr.push(randint(randint(1000)));
  }
  return arr;
};
const thirdMax = (nums) => {
  let top3 = [];
  let set = new Set();
  for (let i = 0; i < nums.length; i++) {
    set.add(nums[i]);
  }
  nums = Array.from(set);
  console.log(nums);
  for (let i = 0; i < nums.length; i++) {
    if (top3.length < 3) {
      top3.push(nums[i]);
      top3.sort((a, b) => {
        return a - b;
      });
    } else if (nums[i] > top3[0]) {
      top3[0] = nums[i];
      top3.sort((a, b) => {
        return a - b;
      });
    }
  }

  console.log(top3);
  top3.sort((a, b) => {
    return a - b;
  });
  if (top3.length === 3) {
    return top3[0];
  } else {
    return top3[top3.length - 1];
  }
};
//--------------------main----------------------------------------------------
let arr = random_array();
let top3 = thirdMax(arr);
console.log(
  arr.sort((a, b) => {
    return a - b;
  })
);
console.log(top3);
