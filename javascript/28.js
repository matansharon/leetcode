// Implement strStr().

// Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

// Clarification:

// What should we return when needle is an empty string? This is a great question to ask during an interview.

// For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

// Example 1:

// Input: haystack = "hello", needle = "ll"
// Output: 2
// Example 2:

// Input: haystack = "aaaaa", needle = "bba"
// Output: -1
// Example 3:

// Input: haystack = "", needle = ""
// Output: 0
 

// Constraints:

// 0 <= haystack.length, needle.length <= 5 * 104
// haystack and needle consist of only lower-case English characters.

const random_word = function () {
  const a_b = "abcdefghijklmnopqrstuvwxyz";
  const len1 = Math.floor(Math.random() * 100) + 1;
  let res = "";
  for (let i = 0; i < len1; i++) {
    res += a_b[Math.floor(Math.random() * a_b.length)];
  }
  return res;
};
const strStr = function (haystack, needle) {
  if (haystack.length === 0 && needle.length === 0) {
    return 0;
  }
  for (let i = 0; i < haystack.length; i++) {
    if (haystack[i] === needle[0]) {
      console.log(haystack.slice(i, i + needle.length));
      if (haystack.slice(i, i + needle.length) === needle) {
        return i;
      }
    }
  }
  return -1;
};
//-------------------------------main--------------------------

// const arr = [];
const word = random_word();

// let len1 = Math.floor(Math.random() * 20);
// for (let i = 0; i < len1; i++) {
//   arr.push(random_word());
// }
const start = Math.floor(Math.random() * 20);
const end = Math.floor(Math.random() * 10);
const target = random_word().slice(start, start + 2);
// target=arr[4]
console.log(target, word);
console.log(strStr(word, target));
console.log(strStr("", ""));

