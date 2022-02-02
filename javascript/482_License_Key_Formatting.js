// You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

// We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

// Return the reformatted license key.

 

// Example 1:

// Input: s = "5F3Z-2e-9-w", k = 4
// Output: "5F3Z-2E9W"
// Explanation: The string s has been split into two parts, each part has 4 characters.
// Note that the two extra dashes are not needed and can be removed.
// Example 2:

// Input: s = "2-5g-3-J", k = 2
// Output: "2-5G-3J"
// Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
 

// Constraints:

// 1 <= s.length <= 105
// s consists of English letters, digits, and dashes '-'.
// 1 <= k <= 104


const clean_string = (s) => {
  let res = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] !== "-") {
      res += s[i];
    }
  }
  console.log(res.toUpperCase());
  return res.toUpperCase();
};

// const licenseKeyFormatting = (s, k) => {
//   s = Array.from(clean_string(s));

//   let res_s = [];
//   let curr = 0;
//   for (let i = s.length - 1; i > -1; i--) {
//     if (curr < k) {
//       res_s.push(s[i]);
//       curr++;
//     } else {
//       res_s.push("-");
//       res_s.push(s[i]);
//       curr = 0;
//     }
//   }

//   res_s = res_s.reverse().join("");
//   console.log(res_s);
//   return res_s;
// };

const licenseKeyFormatting = (s, k) => {
  res = [];
  curr = k;
  s = Array.from(s).reverse().join("");
  for (let i = 0; i < s.length; i++) {
    if (s[i] !== "-") {
      if (curr === 0) {
        res.push("-");
        curr = k;
      }
      res.push(s[i].toUpperCase());
      curr--;
    }
  }
  return res.reverse().join("");
};
//--------------------main----------------------------------------------------------------------
licenseKeyFormatting("5F3Z-2e-9-ww", 2);
