// The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

// Given two integers x and y, return the Hamming distance between them.

 

// Example 1:

// Input: x = 1, y = 4
// Output: 2
// Explanation:
// 1   (0 0 0 1)
// 4   (0 1 0 0)
//        ↑   ↑
// The above arrows point to positions where the corresponding bits are different.
// Example 2:

// Input: x = 3, y = 1
// Output: 1
 

// Constraints:

// 0 <= x, y <= 231 - 1


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
// const hammingDistance = (x, y) => {
//   let a = x.toString(2);
//   let b = y.toString(2);
//   let short;
//   let long;
//   if (a.legnth > b.length) {
//     long = a;
//     b = short;
//   } else {
//     long = b;
//     short = a;
//   }

//   short = short.split("").reverse();

//   long = long.split("").reverse();
//   short;
//   long;
//   let res = 0;
//   for (let i = 0; i < short.length; i++) {
//     if (short[i] !== long[i]) {
//       res++;
//     }
//   }
//   for (let i = short.length; i < long.length; i++) {
//     if (long[i] === "1") {
//       res++;
//     }
//   }

//   console.log(res);
//   return res;
// };

const hammingDistance = (x, y) => {
  let xor = (x ^ y).toString(2);
  console.log(xor);
  let res = 0;
  for (let i = 0; i < xor.length; i++) {
    if (xor[i] === "1") {
      res++;
    }
  }
  return res;
};
//--------------------main----------------------------------------------------
hammingDistance(1501377268, 258791155);
