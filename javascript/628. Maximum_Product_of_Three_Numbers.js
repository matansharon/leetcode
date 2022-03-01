// Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

// Example 1:

// Input: nums = [1,2,3]
// Output: 6
// Example 2:

// Input: nums = [1,2,3,4]
// Output: 24
// Example 3:

// Input: nums = [-1,-2,-3]
// Output: -6
 

// Constraints:

// 3 <= nums.length <= 104
// -1000 <= nums[i] <= 1000


/**
 * @param {number[]} nums
 * @return {number}
 */

const maximumProduct=(nums)=>{
  nums.sort((a,b)=>{return a-b})
  let len=nums.length;
  let res=nums[len-1]*nums[len-2]*nums[len-3];
  if(nums[0]<0&&nums[1]<0){
    if(nums[0]*nums[1]*nums[len-1]>res){res=nums[0]*nums[1]*nums[len-1]}
  }
  return res;

}
