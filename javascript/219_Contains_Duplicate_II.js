// Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

// Example 1:

// Input: nums = [1,2,3,1], k = 3
// Output: true
// Example 2:

// Input: nums = [1,0,1,1], k = 1
// Output: true
// Example 3:

// Input: nums = [1,2,3,1,2,3], k = 2
// Output: false
 

// Constraints:

// 1 <= nums.length <= 105
// -109 <= nums[i] <= 109
// 0 <= k <= 105


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_array = () => {
  let len = randint(100000);
  let nums = [];
  for (let i = 0; i < len; i++) {
    // if (Math.random() < 0.5) {
    //   nums.push(randint(1000000000));
    // } else {
    //   nums.push(randint(1000000000) * -1);
    // }
    nums.push(randint(100000));
  }
  // console.log(nums);
  return nums;
};
const containsNearbyDuplicate = (nums, k) => {
  let map=new Map();
  for(let i=0; i < nums.length; i++) {
    if(map.has(nums[i])===false) {
      map.set(nums[i],i)
    }
    else{
      if(Math.abs(map.get(nums[i])-i)<=k){return true;}
      else{
        map.set(nums[i],i)
      }
    }
  }
  return false;
};
//--------------------main----------------------------------------------------
let arr = random_array();
console.log(containsNearbyDuplicate(arr,,5));
