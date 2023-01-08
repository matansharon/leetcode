// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

// Example 1:

// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2]
// Example 2:

// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [9,4]
// Explanation: [4,9] is also accepted.
 

// Constraints:

// 1 <= nums1.length, nums2.length <= 1000
// 0 <= nums1[i], nums2[i] <= 1000


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_array = () => {
  let set = new Set();
  let len = randint(1000);
  for (let i = 0; i < len; i++) {
    set.add(randint(1000));
  }
  // console.log(Array.from(set));
  return Array.from(set);
};
const intersection = (nums1, nums2) => {
  let map1 = new Map();
  let res = new Set();
  for (let i = 0; i < nums1.length; i++) {
    map1.set(nums1[i]);
  }
  for (let i = 0; i < nums2.length; i++) {
    if (map1.has(nums2[i])) {
      res.add(nums2[i]);
    }
  }
  return Array.from(res);
};
//--------------------main----------------------------------------------------
let arr1 = random_array();
// console.log(arr1);
let arr2 = random_array();
console.log(intersection(arr1, arr2));
