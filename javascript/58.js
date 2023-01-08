// Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

// A word is a maximal substring consisting of non-space characters only.

 

// Example 1:

// Input: s = "Hello World"
// Output: 5
// Explanation: The last word is "World" with length 5.
// Example 2:

// Input: s = "   fly me   to   the moon  "
// Output: 4
// Explanation: The last word is "moon" with length 4.
// Example 3:

// Input: s = "luffy is still joyboy"
// Output: 6
// Explanation: The last word is "joyboy" with length 6.
 

// Constraints:

// 1 <= s.length <= 104
// s consists of only English letters and spaces ' '.
// There will be at least one word in s.


const randint = function (val) {
  return Math.floor(Math.random() * val);
};

const random_text = () => {
  const a_b = "abcdefghijklmnopqrstuvwxyz";
  let res = "";
  if (Math.random() > 0.5) {
    res += " ".repeat(randint(10));
  }
  let num_of_words = Math.floor(Math.random() * 20) + 1;
  for (let i = 0; i < num_of_words; i++) {
    let len = randint(10);
    for (let j = 0; j < len; j++) {
      res += a_b[randint(a_b.length)];
    }
    res += " ".repeat(randint(10));
  }
  return res;
};

let text = random_text();
console.log(text);
// loop to find the last charchter;
let last = -1;
for (let i = text.length - 1; i >= 0; i--) {
  if (text[i] !== " ") {
    last = i;
    break;
  }
}
//loop to find the first character
let start = last - 1;
for (let i = last - 1; i > -1; i--) {
  if (text[i] === " ") {
    start = i;
    break;
  }
}
console.log(text);
temp = text.slice(start, last + 1);
console.log(last - start);
return last - start;
// console.log(start, last, text.slice(start, last + 1));
//
