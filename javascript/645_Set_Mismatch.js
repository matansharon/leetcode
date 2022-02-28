// You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

// You are given an integer array nums representing the data status of this set after the error.

// Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

// Example 1:

// Input: nums = [1,2,2,4]
// Output: [2,3]
// Example 2:

// Input: nums = [1,1]
// Output: [1,2]
 

// Constraints:

// 2 <= nums.length <= 104
// 1 <= nums[i] <= 104
// Accepted
// 159.5K



/**
 * @param {number[]} nums
 * @return {number[]}
 */
const findErrorNums=(nums)=>{
  let all_numbers=new Map();
  for(let i=1;i<=nums.length;i++){
    all_numbers.set(i,0)
  }
  let res=[-1,-1]
  for(let i=0;i<nums.length;i++){
    if(all_numbers.has(nums[i])){
      let temp=all_numbers.get(nums[i])
      all_numbers.set(nums[i],temp+1);
    }
    
  
}
// console.log(all_numbers)
for([key,val] of all_numbers.entries()){
  if(val===0){res[1]=key}
  if(val>1){res[0]=key}
}
// console.log(res)
return res;

}
