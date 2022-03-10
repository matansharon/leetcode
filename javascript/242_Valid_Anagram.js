// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

// Example 1:

// Input: s = "anagram", t = "nagaram"
// Output: true
// Example 2:

// Input: s = "rat", t = "car"
// Output: false
 

// Constraints:

// 1 <= s.length, t.length <= 5 * 104
// s and t consist of lowercase English letters.
 

// Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_word = () => {
  const a_b = "abcdefghijklmnopqrstuvwxyz";
  let len = randint(100);
  let res = "";
  for (let i = 0; i < len; i++) {
    res += a_b[randint(a_b.length)];
  }
  return res;
};
const isAnagram = (s, t) => {
  let map_s = new Map();
  let map_t = new Map();
  if (s.length !== t.length) {
    return false;
  }
  for (let i = 0; i < s.length; i++) {
    if (map_s.has(s[i])) {
      map_s.set(s[i], map_s.get(s[i]) + 1);
    } else {
      map_s.set(s[i], 1);
    }
    if (map_t.has(t[i])) {
      map_t.set(t[i], map_t.get(t[i]) + 1);
    } else {
      map_t.set(t[i], 1);
    }
  }
  console.log(map_t);
  for (let item of map_s.entries()) {
    console.log(item[0], item[1]);
    if (map_t.has(item[0]) === false || map_t.get(item[0]) !== item[1]) {
      return false;
    }
  }
  return true;
};
//--------------------main----------------------------------------------------
console.log(isAnagram("abbc", "bcba"));
