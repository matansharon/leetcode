// Write a function that reverses a string. The input string is given as an array of characters s.

// You must do this by modifying the input array in-place with O(1) extra memory.

 

// Example 1:

// Input: s = ["h","e","l","l","o"]
// Output: ["o","l","l","e","h"]
// Example 2:

// Input: s = ["H","a","n","n","a","h"]
// Output: ["h","a","n","n","a","H"]
 

// Constraints:

// 1 <= s.length <= 105
// s[i] is a printable ascii character.


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_word_array = () => {
  let letter =
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_+{}:?><,./;'[";
  let len = randint(10);
  let res = [];
  for (let i = 0; i < len; i++) {
    res.push(letter[randint(letter.length)]);
  }
  return res;
};
const reverseString = (arr) => {
  let low = 0;
  let high = arr.length - 1;
  while (low < high) {
    let temp = arr[low];
    arr[low] = arr[high];
    arr[high] = temp;
    low++;
    high--;
  }
};
//--------------------main----------------------------------------------------
let arr = random_word_array();
console.log(arr);
reverseString(arr);
console.log(arr);
