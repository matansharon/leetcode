// Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

// Example 1:

// Input: s = "leetcode"
// Output: 0
// Example 2:

// Input: s = "loveleetcode"
// Output: 2
// Example 3:

// Input: s = "aabb"
// Output: -1
 

// Constraints:

// 1 <= s.length <= 105
// s consists of only lowercase English letters.


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_word = () => {
  let a_b = "abcdefghijklmnopqrsyuvwxyz";
  let res = "";
  let len = randint(100);
  for (let i = 0; i < len; i++) {
    res += a_b[randint(a_b.length)];
  }
  return res;
};
const firstUniqChar = (s) => {
  console.log(s);
  let map = new Map();
  for (let i = 0; i < s.length; i++) {
    if (!map.has(s[i])) {
      map.set(s[i], 1);
    } else {
      map.set(s[i], map.get(s[i]) + 1);
    }
  }
  // console.log(map)
  for (let i = 0; i < s.length; i++) {
    if (map.get(s[i]) === 1) {
      return i;
    }
  }
  return -1;
};
//--------------------main----------------------------------------------------
console.log(firstUniqChar(random_word()));
