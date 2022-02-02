// Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

// Example 1:

// Input: nums = [1,1,0,1,1,1]
// Output: 3
// Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
// Example 2:

// Input: nums = [1,0,1,1,0,1]
// Output: 2
 

// Constraints:

// 1 <= nums.length <= 105
// nums[i] is either 0 or 1.


const findMaxConsecutiveOnes = (nums) => {
  let con = 0;
  let res = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 1) {
      con++;
    } else {
      if (con > res) {
        res = con;
      }
      con = 0;
    }
  }
  if (con > res) {
    res = con;
  }
  console.log(res);
  return res;
};
//--------------------main----------------------------------------------------------------------
findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]);
