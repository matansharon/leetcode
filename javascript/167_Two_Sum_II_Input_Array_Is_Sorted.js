// # Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

// # Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

// # The tests are generated such that there is exactly one solution. You may not use the same element twice.

 

// # Example 1:

// # Input: numbers = [2,7,11,15], target = 9
// # Output: [1,2]
// # Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
// # Example 2:

// # Input: numbers = [2,3,4], target = 6
// # Output: [1,3]
// # Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
// # Example 3:

// # Input: numbers = [-1,0], target = -1
// # Output: [1,2]
// # Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

// # Constraints:

// # 2 <= numbers.length <= 3 * 104
// # -1000 <= numbers[i] <= 1000
// # numbers is sorted in non-decreasing order.
// # -1000 <= target <= 1000
// # The tests are generated such that there is exactly one solution.


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_arr = () => {
  let res = [];
  let num = 0;
  while (num < 20) {
    num += randint(5) + 1;
    res.push(num);
  }
  return res;
};
var twoSum = function (numbers, target) {
  low = 0;
  high = numbers.length - 1;
  sum = numbers[high] + numbers[low];
  console.log(sum);
  while (low < high) {
    sum = numbers[high] + numbers[low];
    if (sum === target) {
      break;
    } else if (sum > target) {
      high--;
    } else {
      low++;
    }
  }
  return [low + 1, high + 1];
};
//--------------------main----------------------------------------------------et temp = random_arr();
let arr = random_arr();
let a = arr[randint(arr.length)];
let b = arr[randint(arr.length)];
let res = twoSum(arr, a, b);
