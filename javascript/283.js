// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Note that you must do this in-place without making a copy of the array.

 

// Example 1:

// Input: nums = [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Example 2:

// Input: nums = [0]
// Output: [0]
 

// Constraints:

// 1 <= nums.length <= 104
// -231 <= nums[i] <= 231 - 1
 

// Follow up: Could you minimize the total number of operations done?


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_arr = () => {
  let len = randint(10);
  let arr = [];
  for (let i = 0; i < len; i++) {
    if (Math.random() > 0.7) {
      arr.push(0);
    } else {
      arr.push(randint(100));
    }
  }
  return arr;
};
const moveZeroes = (arr) => {
  let map = new Map();
  let pos = 0;
  let num_of_zeros = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== 0) {
      map.set(pos, arr[i]);
      pos++;
    } else {
      num_of_zeros++;
    }
  }
  map.set("0", num_of_zeros);
  let last = -1;
  map.forEach((v, k) => {
    if (k !== "0") {
      arr[k] = v;
      last = k;
    } else {
      last++;
      console.log(last);
      for (let i = 0; i < v; i++) {
        arr[last] = 0;
        last++;
      }
    }
  });
};
//--------------------main----------------------------------------------------
let arr = random_arr();
console.log(arr);

console.log(moveZeroes(arr));
console.log(arr);
