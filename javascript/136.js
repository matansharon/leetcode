// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

// You must implement a solution with a linear runtime complexity and use only constant extra space.

 

// Example 1:

// Input: nums = [2,2,1]
// Output: 1
// Example 2:

// Input: nums = [4,1,2,1,2]
// Output: 4
// Example 3:

// Input: nums = [1]
// Output: 1
 

// Constraints:

// 1 <= nums.length <= 3 * 104
// -3 * 104 <= nums[i] <= 3 * 104
// Each element in the array appears twice except for one element which appears only once.


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_arr = () => {
  let len = randint(20);
  let res = [];
  for (let i = 0; i < len; i++) {
    res.push(i);
    res.push(i);
  }
  // console.log(res);
  return res;
};

const singleNumber = (nums) => {
  let dic = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (dic.has(nums[i])) {
      dic.set(nums[i], 2);
    } else dic.set(nums[i], 1);
  }
  for (const [k, v] of dic.entries()) {
    if (v === 1) {
      return k;
    }
  }
};

//--------------------main----------------------------------------------------
let arr = random_arr();
// console.log(arr);
arr.pop();
arr.sort(() => 0.5 - Math.random());
// console.log(arr);
const res = singleNumber(arr);
