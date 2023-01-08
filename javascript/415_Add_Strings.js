// Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

// You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

// Example 1:

// Input: num1 = "11", num2 = "123"
// Output: "134"
// Example 2:

// Input: num1 = "456", num2 = "77"
// Output: "533"
// Example 3:

// Input: num1 = "0", num2 = "0"
// Output: "0"
 

// Constraints:

// 1 <= num1.length, num2.length <= 104
// num1 and num2 consist of only digits.
// num1 and num2 don't have any leading zeros except for the zero itself.


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_number_as_string = () => {
  let numbers = "1234567890";
  let len = randint(10) - 1;
  let res = numbers[randint(numbers.length - 1)];
  for (let i = 0; i < len; i++) {
    res += numbers[randint(numbers.length)];
  }
  return res;
};
const addStrings = (num1, num2) => {
  let arr1 = Array.from(num1);
  let arr2 = Array.from(num2);
  let res = [];
  arr1.reverse();
  arr2.reverse();
  let len = Math.max(arr1.length, arr2.length);
  console.log(len);
  let carry = 0;
  for (let i = 0; i < len; i++) {
    let a = arr1[i];
    let b = arr2[i];
    if (a !== undefined && b !== undefined) {
      let sum = Number.parseInt(a) + Number.parseInt(b) + carry;
      if (sum >= 10) {
        res.push(sum - 10);
        carry = 1;
      } else {
        res.push(sum);
        carry = 0;
      }
    } else if (a !== undefined && b === undefined) {
      let sum = Number.parseInt(a) + carry;
      if (sum >= 10) {
        res.push(sum - 10);
        carry = 1;
      } else {
        res.push(sum);
        carry = 0;
      }
    } else if ((a === undefined) & (b !== undefined)) {
      let sum = Number.parseInt(b) + carry;
      if (sum >= 10) {
        res.push(sum - 10);
        carry = 1;
      } else {
        res.push(sum);
        carry = 0;
      }
    }
  } //end of for
  if (carry === 1) {
    res.push("1");
  }
  return res.reverse().join("");
}; //end of function addStrings

//--------------------main----------------------------------------------------

