// We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

// Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

// A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

 

// Example 1:

// Input: nums = [1,3,2,2,5,2,3,7]
// Output: 5
// Explanation: The longest harmonious subsequence is [3,2,2,2,3].
// Example 2:

// Input: nums = [1,2,3,4]
// Output: 2
// Example 3:

// Input: nums = [1,1,1,1]
// Output: 0
 

// Constraints:

// 1 <= nums.length <= 2 * 104
// -109 <= nums[i] <= 109


const findLHS=(nums)=>{
    let map=new Map();
    let res=0;
    for(let i=0;i<nums.length;i++){
        if(map.has(nums[i])){map.set(nums[i],map.get(nums[i])+1);}
        else{map.set(nums[i],1)}
    }
    let keys=[]
    for(let i of map.keys()){
        keys.push(i)
    }
    keys.sort((a,b)=>{return a-b})
    for(let i=0;i<keys.length-1;i++){
        let diff=keys[i+1]-keys[i]
        let temp=0;
        if(diff===1){temp=map.get(keys[i+1])+map.get(keys[i])}
        if(temp>res){res=temp}
    }
    return res;
}

  //--------------------main----------------------------------------------------
console.log(findLHS([1,3,2,2,5,2,3,7]))
