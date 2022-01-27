// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

// Example 1:

// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2,2]
// Example 2:

// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [4,9]
// Explanation: [9,4] is also accepted.
 

// Constraints:

// 1 <= nums1.length, nums2.length <= 1000
// 0 <= nums1[i], nums2[i] <= 1000
 

// Follow up:

// What if the given array is already sorted? How would you optimize your algorithm?
// What if nums1's size is small compared to nums2's size? Which algorithm is better?
// What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_array = () => {
  let arr = [];
  let len = randint(30) + 1;
  for (let i = 0; i < len; i++) {
    arr.push(randint(10));
  }
  // console.log(Array.from(set));
  return arr;
};
const intersect = (nums1, nums2) => {
  console.log(nums1);
  let map1 = new Map();
  let map2 = new Map();
  let res = [];
  for (let i = 0; i < nums1.length; i++) {
    if (map1.has(nums1[i])) {
      map1.set(nums1[i], map1.get(nums1[i]) + 1);
    } else map1.set(nums1[i], 1);
  }

  for (let i = 0; i < nums2.length; i++) {
    if (map2.has(nums2[i])) {
      map2.set(nums2[i], map2.get(nums2[i]) + 1);
    } else map2.set(nums2[i], 1);
  }
  for ([key, val] of map1.entries()) {
    if (map2.has(key)) {
      if (map1.get(key) > map1.get(key)) {
        for (let i = 0; i < map1.get(key); i++) {
          res.push(key);
        }
      } else {
        for (let i = 0; i < map2.get(key); i++) {
          res.push(key);
        }
      }
    }
  }
  console.log(res);
};

//--------------------main----------------------------------------------------
let arr1 = random_array();
// console.log(arr1);
let arr2 = random_array();
console.log(intersect(arr1, arr2));
