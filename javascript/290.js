// Given a pattern and a string s, find if s follows the same pattern.

// Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

// Example 1:

// Input: pattern = "abba", s = "dog cat cat dog"
// Output: true
// Example 2:

// Input: pattern = "abba", s = "dog cat cat fish"
// Output: false
// Example 3:

// Input: pattern = "aaaa", s = "dog cat cat dog"
// Output: false
 

// Constraints:

// 1 <= pattern.length <= 300
// pattern contains only lower-case English letters.
// 1 <= s.length <= 3000
// s contains only lowercase English letters and spaces ' '.
// s does not contain any leading or trailing spaces.
// All the words in s are separated by a single space.


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const wordPattern = (pattern, s) => {
  let arr = s.split(" ");

  if (arr.length !== pattern.length) {
    return false;
  }
  let map_p_s = new Map();
  let map_s_p = new Map();
  for (let i = 0; i < arr.length; i++) {
    if (map_p_s.has(pattern[i]) === false) {
      map_p_s.set(pattern[i], arr[i]);
    } else {
      if (map_p_s.get(pattern[i]) !== arr[i]) {
        return false;
      }
    }

    if (map_s_p.has(arr[i]) === false) {
      map_s_p.set(arr[i], pattern[i]);
    } else {
      if (map_s_p.get(arr[i]) !== pattern[i]) {
        return false;
      }
    }
    console.log(map_p_s.size);
    console.log(map_s_p.size);
    if (map_p_s.size !== map_s_p.size) {
      return false;
    }
  }
  return true;
};
//--------------------main----------------------------------------------------
console.log(wordPattern("abba", "dog cat cat dog"));
