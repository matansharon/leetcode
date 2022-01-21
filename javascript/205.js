// Given two strings s and t, determine if they are isomorphic.

// Two strings s and t are isomorphic if the characters in s can be replaced to get t.

// All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

// Example 1:

// Input: s = "egg", t = "add"
// Output: true
// Example 2:

// Input: s = "foo", t = "bar"
// Output: false
// Example 3:

// Input: s = "paper", t = "title"
// Output: true
 

// Constraints:

// 1 <= s.length <= 5 * 104
// t.length == s.length
// s and t consist of any valid ascii character.


//---------------------------------------------------------------------------this sulotion is 39/43 test cases


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_word = () => {
  const a_b = "abcdefghijklmnopqrstuvwxyz";
  let len = randint(50);
  let res = "";
  for (let i = 0; i < len; i++) {
    res += a_b[randint(a_b.length)];
  }
  return res;
};
const isIsomorphic = (s, t) => {
  console.log(convert_to_index_string(s), convert_to_index_string(t));
  return convert_to_index_string(s) === convert_to_index_string(t);
};
const convert_to_index_string = (s) => {
  let arr = [];
  let map = new Map();
  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i]) === false) {
      map.set(s[i], i);
    }
    arr.push(map.get(s[i]));
  }
  let res = "";
  for (let i = 0; i < arr.length; i++) {
    res += arr[i];
  }
  return res;
};
//--------------------main----------------------------------------------------
console.log(
  isIsomorphic("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck")
);



