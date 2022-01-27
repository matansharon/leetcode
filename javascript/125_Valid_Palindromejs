// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

// Given a string s, return true if it is a palindrome, or false otherwise.

 

// Example 1:

// Input: s = "A man, a plan, a canal: Panama"
// Output: true
// Explanation: "amanaplanacanalpanama" is a palindrome.
// Example 2:

// Input: s = "race a car"
// Output: false
// Explanation: "raceacar" is not a palindrome.
// Example 3:

// Input: s = " "
// Output: true
// Explanation: s is an empty string "" after removing non-alphanumeric characters.
// Since an empty string reads the same forward and backward, it is a palindrome.
 

// Constraints:

// 1 <= s.length <= 2 * 105
// s consists only of printable ASCII characters.


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const randchar = () => {
  const a_b = "abcdefghijklmnopqrstuvwxyz";
  const res = a_b[randint(a_b.length)];
  // console.log()
  return res;
};
const rand_ugly_char = () => {
  const a_b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const numbers = "1234567890";
  const symbols = "!@ #$%^ &* ()_+~{}?>< ";
  const chance = Math.random();
  if (chance < 1 / 3) {
    return a_b[randint(a_b.length)];
  }
  if (chance >= 1 / 3 && chance < 2 / 3) {
    return numbers[randint(numbers.length)];
  }
  if (chance >= 2 / 3) {
    return symbols[randint(symbols.length)];
  }
};
const gen_pali = () => {
  const len = randint(15) + 1;

  let pali = "";
  for (let i = 0; i < len; i++) {
    pali += randchar();
  }
  let no_pali = "";
  for (let i = 0; i < len; i++) {
    no_pali += rand_ugly_char();
  }
  let res = "";
  for (let i = 0; i < len; i++) {
    res += pali[i];
    res += no_pali[i];
  }
  for (let i = pali.length - 1; i > -1; i--) {
    res += pali[i];
    res += rand_ugly_char();
  }
  return res;
};
const gen_non_pali = () => {
  const len = randint(100);
  let res = "";
  for (let i = 0; i < len; i++) {
    let chance = Math.random();
    if (chance > 0.5) {
      res += randchar();
    } else {
      res += rand_ugly_char();
    }
  }
  return res;
};
const clean_string = (str) => {
  let res = "";
  for (let i = 0; i < str.length; i++) {
    if (str[i].charCodeAt() > 98 && str[i].charCodeAt() < 122) {
      res += str[i];
      //this comments lines is for the test cases at leetcode
      // } else if (str[i].charCodeAt() >= 65 && str[i].charCodeAt() <= 90) {
      //   res += str[i].toLowerCase();
      // } else if (str[i].charCodeAt() >= 48 && str[i].charCodeAt() <= 57) {
      //   res += str[i];
    }
  }
  return res;
};
const isPalindrome = (s) => {
  let back = "";
  for (let i = s.length - 1; i > -1; i--) {
    back += s[i];
  }
  // console.log(back);
  return back === s;
};
//--------------------main----------------------------------------------------
for (let i = 0; i < 1; i++) {
  let chance = Math.random();
  if (chance > 0.5) {
    let pali = gen_pali();
    console.log(pali);
    let clean_pali = clean_string(pali);
    console.log(clean_pali);
    console.log(isPalindrome(clean_pali));
  } else {
    let non_pali = gen_non_pali();
    console.log(non_pali);
    let clean_non_pali = clean_string(non_pali);
    console.log(clean_non_pali);
    console.log(clean_non_pali);
    console.log(isPalindrome(clean_non_pali));
  }
}
