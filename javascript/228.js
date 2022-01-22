// You are given a sorted unique integer array nums.

// Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

// Each range [a,b] in the list should be output as:

// "a->b" if a != b
// "a" if a == b
 

// Example 1:

// Input: nums = [0,1,2,4,5,7]
// Output: ["0->2","4->5","7"]
// Explanation: The ranges are:
// [0,2] --> "0->2"
// [4,5] --> "4->5"
// [7,7] --> "7"
// Example 2:

// Input: nums = [0,2,3,4,6,8,9]
// Output: ["0","2->4","6","8->9"]
// Explanation: The ranges are:
// [0,0] --> "0"
// [2,4] --> "2->4"
// [6,6] --> "6"
// [8,9] --> "8->9"
 

// Constraints:

// 0 <= nums.length <= 20
// -231 <= nums[i] <= 231 - 1
// All the values of nums are unique.
// nums is sorted in ascending order.

const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_arr = () => {
  let len = randint(20);
  let res = [];
  for (let i = 0; i < len; i++) {
    if (Math.random() < 0.5) {
      res.push(i);
    }
  }
  return res;
};
var summaryRanges = function (nums) {
  if (nums.length === 0) {
    return [];
  }

  if (nums.length === 1) {
    nums[0] = nums[0].toString();
    return nums;
  }

  let start = nums[0];
  let end = null;
  const output = [];

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] !== nums[i - 1] + 1) {
      let item;
      if (!!end && start !== end) {
        item = `${start}->${end}`;
      } else {
        item = `${start}`;
      }
      start = nums[i];
      end = nums[i];
      output.push(item);
    } else {
      end = nums[i];
    }
  }

  let item;
  if (!!end && start !== end) {
    item = `${start}->${end}`;
  } else {
    item = `${start}`;
  }
  output.push(item);

  return output;
};
//--------------------main----------------------------------------------------
let arr = random_arr();
console.log(arr);
console.log(summaryRanges([0, 1, 2, 4, 5, 7]));
