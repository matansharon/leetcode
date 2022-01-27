// Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

// Each letter in magazine can only be used once in ransomNote.

 

// Example 1:

// Input: ransomNote = "a", magazine = "b"
// Output: false
// Example 2:

// Input: ransomNote = "aa", magazine = "ab"
// Output: false
// Example 3:

// Input: ransomNote = "aa", magazine = "aab"
// Output: true
 

// Constraints:

// 1 <= ransomNote.length, magazine.length <= 105
// ransomNote and magazine consist of lowercase English letters.


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_word = (len) => {
  let a_b = "abcdefghijklmnopqrsyuvwxyz";
  let res = "";
  for (let i = 0; i < len; i++) {
    res += a_b[randint(a_b.length)];
  }
  return res;
};
const canConstruct = (ransom, magazine) => {
  let magazine_map = new Map();
  let ransom_map = new Map();
  for (let i = 0; i < magazine.length; i++) {
    if (magazine_map.has(magazine[i])) {
      magazine_map.set(magazine[i], magazine_map.get(magazine[i]) + 1);
    } else {
      magazine_map.set(magazine[i], 1);
    }
  }

  for (let i = 0; i < ransom.length; i++) {
    if (ransom_map.has(ransom[i])) {
      ransom_map.set(ransom[i], ransom_map.get(ransom[i]) + 1);
    } else {
      ransom_map.set(ransom[i], 1);
    }
  }
  console.log(ransom_map);
  console.log(magazine_map);
  for ([key, val] of ransom_map) {
    console.log(key, val);
    if (magazine_map.has(key)) {
      if (magazine_map.get(key) < val) {
        return false;
      }
    } else {
      return false;
    }
  }
  return true;
};
//--------------------main----------------------------------------------------
let magazine = random_word(randint(10) + 10);
let ransom = random_word(randint(10));
console.log(
  canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
);
