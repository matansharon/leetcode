// Given a string num which represents an integer, return true if num is a strobogrammatic number.

// A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

// Example 1:

// Input: num = "69"
// Output: true
// Example 2:

// Input: num = "88"
// Output: true
// Example 3:

// Input: num = "962"
// Output: false
 

// Constraints:

// 1 <= num.length <= 50
// num consists of only digits.
// num does not contain any leading zeros except for zero itself.



const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_word = () => {
  const numbers = "1234567890";
  let len = randint(10);
  let res = numbers[randint(numbers.length - 1)];
  for (let i = 0; i < len; i++) {
    res += numbers[randint(numbers.length)];
  }
  return res;
};

const isStrobogrammatic = (num) => {
  if (num === "6" || num === "9") {
    return false;
  }
  let map = new Map();
  map.set("2");
  map.set("3");
  map.set("4");
  map.set("5");
  map.set("7");

  for (let i = 0; i < num.length; i++) {
    if (map.has(num[i])) {
      return false;
    }
  }
  let low = 0;
  let high = num.length - 1;
  while (low < high) {
    if (num[low] === "1" && num[high] !== "1") {
      return false;
    }
    if (num[low] === "0" && num[high] !== "0") {
      return false;
    }
    if (num[low] === "8" && num[high] !== "8") {
      return false;
    }
    if (num[low] === "6" && num[high] !== "9") {
      return false;
    }
    if (num[low] === "9" && num[high] !== "6") {
      return false;
    }
    low++;
    high--;
  }
  if (low === high && (num[low] === "6" || num[low] === "9")) {
    return false;
  }
  return true;
};
//--------------------main----------------------------------------------------
// for (let i = 0; i < 10; i++) {
//   console.log(random_word());
// }
console.log(isStrobogrammatic("11"));
