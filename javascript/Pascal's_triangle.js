// Given an integer numRows, return the first numRows of Pascal's triangle.

// In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

// Example 1:

// Input: numRows = 5
// Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
// Example 2:

// Input: numRows = 1
// Output: [[1]]
 

// Constraints:

// 1 <= numRows <= 30


// const randint = (val) => {
//   return Math.floor(Math.random() * val);
// };
const generate = (numOfRows) => {
  if (numOfRows === 1) {
    return [[1]];
  }
  if (numOfRows === 2) {
    return [[1], [1, 1]];
  }
  let res = [[1], [1, 1]];
  for (let col = 2; col < numOfRows; col++) {
    let arr = new Array(col + 1);
    arr[0] = 1;
    arr[col] = 1;
    for (let j = 1; j < arr.length - 1; j++) {
      arr[j] = res[col - 1][j - 1] + res[col - 1][j];
    }
    res.push(arr);
  }
  return res;
};
//--------------------main----------------------------------------------------
for (let i = 1; i < 31; i++) {
  console.log(generate(i));
}
