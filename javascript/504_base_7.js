// Given an integer num, return a string of its base 7 representation.

 

// Example 1:

// Input: num = 100
// Output: "202"
// Example 2:

// Input: num = -7
// Output: "-10"
 

// Constraints:

// -107 <= num <= 107

const randint = (val) => {
    return Math.floor(Math.random() * val);
}
const convertToBase=(num) => {
    return num.toString(7)
}
  //--------------------main----------------------------------------------------
  
