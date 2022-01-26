// Given a string s, reverse only all the vowels in the string and return it.

// The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

// Example 1:

// Input: s = "hello"
// Output: "holle"
// Example 2:

// Input: s = "leetcode"
// Output: "leotcede"
 

// Constraints:

// 1 <= s.length <= 3 * 105
// s consist of printable ASCII characters.


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_word_array = () => {
  let letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  let len = randint(20);
  let res = [];
  for (let i = 0; i < len; i++) {
    res.push(letter[randint(letter.length)]);
  }
  return res.join("");
};
const reverseVowels = (s) => {
  // console.log(s);
  let vaowls = new Map();
  vaowls.set("a", null);
  vaowls.set("e", null);
  vaowls.set("i", null);
  vaowls.set("o", null);
  vaowls.set("u", null);
  vaowls.set("A", null);
  vaowls.set("E", null);
  vaowls.set("I", null);
  vaowls.set("O", null);
  vaowls.set("U", null);
  let letters = [];
  let positions = [];
  for (let i = 0; i < s.length; i++) {
    if (vaowls.has(s[i])) {
      letters.push(s[i]);
    }
  }
  let v = letters.length - 1;
  let res = "";
  for (let i = 0; i < s.length; i++) {
    if (vaowls.has(s[i])) {
      res += letters[v];
      v--;
    } else {
      res += s[i];
    }
  }
  // console.log(letters)
  // console.log(s,res);;
  return res;
};
//--------------------main----------------------------------------------------
reverseVowels(random_word_array());
