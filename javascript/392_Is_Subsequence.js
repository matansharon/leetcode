// Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

// A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

// Example 1:

// Input: s = "abc", t = "ahbgdc"
// Output: true
// Example 2:

// Input: s = "axc", t = "ahbgdc"
// Output: false
 

// Constraints:

// 0 <= s.length <= 100
// 0 <= t.length <= 104
// s and t consist only of lowercase English letters.
 

// Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?


//*************************************************************************************************************************************************
//this is a very close solution
//*************************************************************************************************************************************************

const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const isSubsequence = (s, t) => {
  let map_s = new Map();
  let map_t = new Map();
  for (let i = 0; i < s.length; i++) {
    if (!map_s.has(s[i])) {
      map_s.set(s[i], 1);
    } else {
      map_s.set(s[i], map_s.get(s[i]) + 1);
    }
  }
  for (let i = 0; i < t.length; i++) {
    if (!map_t.has(t[i])) {
      map_t.set(t[i], 1);
    } else {
      map_t.set(t[i], map_t.get(t[i]) + 1);
    }
  }
  console.log(map_s);
  console.log(map_t);
  for ([key, value] of map_s.entries()) {
    if (!map_t.has(key)) {
      return false;
    } else {
      if (map_t.get(key) < value) {
        return false;
      }
    }
  }
  return true;
};

//--------------------main----------------------------------------------------
console.log(isSubsequence("axc", "ahbgdc"));



//*************************************************************************************************************************************************
//this is the true solution
//*************************************************************************************************************************************************

const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const isSubsequence = (s, t) => {
  let pos = 0;

  for (let i = 0; i < s.length; i++) {
    console.log(s[i], t[pos]);
    while (true) {
      if (t[pos] === s[i]) {
        pos++;
        break;
      } else {
        pos++;
      }
      if (pos > t.length) {
        return false;
      }
    }
  }
  return true;
};

//--------------------main----------------------------------------------------
console.log(isSubsequence("aaaaaa", "bbaaaa"));

