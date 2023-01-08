// Given two binary strings a and b, return their sum as a binary string.

 

// Example 1:

// Input: a = "11", b = "1"
// Output: "100"
// Example 2:

// Input: a = "1010", b = "1011"
// Output: "10101"
 

// Constraints:

// 1 <= a.length, b.length <= 104
// a and b consist only of '0' or '1' characters.
// Each string does not contain leading zeros except for the zero itself.


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_binary_as_string = () => {
  let res = "";
  let length = randint(10);
  for (let i = 0; i < length; i++) {
    if (Math.random() > 0.5) {
      res += "1";
    } else {
      res += "0";
    }
  }
  return res;
};
const convert_binary_string_to_number = (str) => {
  let res = 0;
  let pow = 0;
  for (let i = str.length - 1; i > -1; i--) {
    res += Number.parseInt(str[i]) * 2 ** pow;
    pow++;
  }
  return res;
};

//-----------------------------------------main----------------------------------------------------
let a_string = random_binary_as_string();
let b_string = random_binary_as_string();
console.log(a_string, b_string);
let a_number = convert_binary_string_to_number(a_string);
let b_number = convert_binary_string_to_number(b_string);
console.log(a_number, b_number);
let res = a_number + b_number;

return res.toString(2);
