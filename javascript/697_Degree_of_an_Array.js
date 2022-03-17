// Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

// Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

// Example 1:

// Input: nums = [1,2,2,3,1]
// Output: 2
// Explanation: 
// The input array has a degree of 2 because both elements 1 and 2 appear twice.
// Of the subarrays that have the same degree:
// [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
// The shortest length is 2. So return 2.
// Example 2:

// Input: nums = [1,2,2,3,1,4,2]
// Output: 6
// Explanation: 
// The degree is 3 because the element 2 is repeated 3 times.
// So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

// Constraints:

// nums.length will be between 1 and 50,000.
// nums[i] will be an integer between 0 and 49,999.


const findShortestSubArray=(nums)=>{
  let map=new Map();
  //for loop to find the max degree
  for(let i=0;i<nums.length;i++){
    if(map.has(nums[i])){
      let temp=map.get(nums[i])+1;
      map.set(nums[i],temp);
    }
    else{
      map.set(nums[i],1)
    }
  }
  let deg=-1
  //for loop to determine if there are more then one value that us the max degree
  for(let val of map.values()){
    if (val>deg){deg=val}
  }
  let all_the_max_deg=[]
  for([key,val] of map.entries()){
    if(val===deg){all_the_max_deg.push(key)}
  }
  let first_last=new Map();
  
  all_the_max_deg.forEach((val)=>{
    first_last.set(val,[-1,-1])
  })
  // console.log(first_last)
  for(let i=0;i<nums.length;i++){
    let temp=first_last.get(nums[i])
    // console.log(temp)
    if(temp){
      if(temp[0]===-1){temp[0]=i}
    }
    
  }
  for(let i=nums.length-1;i>-1;i--){
    let temp=first_last.get(nums[i])
    if(temp){
      if(temp[1]===-1){temp[1]=i}
    }
    
  }
  let res=Number.MAX_VALUE
  for(val of first_last.values()) {
    let temp=Math.abs(val[1]-val[0])
    if(temp<res){res=temp}
    // console.log(temp)    
  }
  // console.log(res)
  return res+1
}
  //--------------------main----------------------------------------------------
console.log(findShortestSubArray([1,2,2,3,1]))
