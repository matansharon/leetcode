// Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

// You must write an algorithm with O(log n) runtime complexity.

 

// Example 1:

// Input: nums = [1,3,5,6], target = 5
// Output: 2
// Example 2:

// Input: nums = [1,3,5,6], target = 2
// Output: 1
// Example 3:

// Input: nums = [1,3,5,6], target = 7
// Output: 4
 

// Constraints:

// 1 <= nums.length <= 104
// -104 <= nums[i] <= 104
// nums contains distinct values sorted in ascending order.
// -104 <= target <= 104


const random_array = function () {
  let arr = [];
  const len = Math.floor(Math.random() * 500000);
  for (let i = 0; i < len; i++) {
    let times = Math.floor(Math.random() * 5) + 1;
    for (let j = 0; j < times; j++) {
      arr.push(i);
    }
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
const bin_search = function (arr, val) {
  let low = 0;
  let high = arr.length - 1;

  while (low < high) {
    let mid = (high + low) / 2;
    if (arr[mid] === val) {
      return mid;
    }
    if (val < arr[mid]) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return low;
};
//------------------------main--------------------------
const arr = random_array();
console.log(arr);
const target = Math.floor(Math.random() * 50) + 100;
console.log(target);
const start = new Date().getTime();
bin_search(arr, target);
const end = new Date().getTime();
const duration = end - start;
console.log(duration);
