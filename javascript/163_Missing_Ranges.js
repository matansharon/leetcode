// You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

// A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

// Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

// Each range [a,b] in the list should be output as:

// "a->b" if a != b
// "a" if a == b
 

// Example 1:

// Input: nums = [0,1,3,50,75], lower = 0, upper = 99
// Output: ["2","4->49","51->74","76->99"]
// Explanation: The ranges are:
// [2,2] --> "2"
// [4,49] --> "4->49"
// [51,74] --> "51->74"
// [76,99] --> "76->99"
// Example 2:

// Input: nums = [-1], lower = -1, upper = -1
// Output: []
// Explanation: There are no missing ranges since there are no missing numbers.
 

// Constraints:

// -109 <= lower <= upper <= 109
// 0 <= nums.length <= 100
// lower <= nums[i] <= upper
// All the values of nums are unique.

const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_arr = () => {
  let a = randint(100);
  let b = randint(100);
  let low = Math.min(a, b);
  let high = Math.max(a, b);
  // console.log(low,high);
  let arr = [];

  for (let i = low; i < high; i++) {
    if (Math.random() > 0.8) {
      arr.push(i);
    }
  }
  return [arr, low, high];
};

var findMissingRanges = function (nums, lower, upper) {
  let low = lower - 1;

  let res = [];

  for (let i = 0; i < nums.length; i++) {
    let curr = upper + 1;
    if (i < nums.length) {
      curr = nums[i];
    }
    if (low + 1 <= curr - 1) {
      res.push(convert_range(low + 1, curr - 1));
    }
    low = curr;
  }
  return res;
};
const convert_range = (low, high) => {
  if (low === high) {
    return "" + low;
  }
  return low + "->" + high;
};
//--------------------main----------------------------------------------------
let temp = random_arr();
let arr = temp[0];
let low = temp[1];
let high = temp[2];
console.log(arr, low, high);
console.log(findMissingRanges(arr, low, high));
