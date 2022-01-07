// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

 

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.
 

// Constraints:

// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lower-case English letters.


/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = function (strs) {
  let min = Number.MAX_VALUE;
  let short = "";
  for (let i = 0; i < strs.length; i++) {
    if (strs[i].length < min) {
      min = strs[i].length;
      short = strs[i];
    }
  }
  console.log(min, short);
  let shortest = all_prefix(short);
  let res = "";
  console.log(shortest);
  shortest.forEach((perfix) => {});
};

const all_prefix = function (str) {
  let arr = new Set();
  for (let i = 1; i < str.length; i++) {
    for (let j = 0; j + i <= str.length; j++) {
      // console.log(str.slice(j,j+i));
      // arr.push(str.slice(j,j+i));
      arr.add(str.slice(j, j + i));
    }
  }
  arr.add(str);
  console.log(arr);
  return arr;
};

console.log(longestCommonPrefix(["matan", "raz", "romi", "my"]));
