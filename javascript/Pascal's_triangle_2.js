// Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

// In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

// Example 1:

// Input: rowIndex = 3
// Output: [1,3,3,1]
// Example 2:

// Input: rowIndex = 0
// Output: [1]
// Example 3:

// Input: rowIndex = 1
// Output: [1,1]
 

// Constraints:

// 0 <= rowIndex <= 33
 

// Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

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
const getRow = (rowIndex) => {
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
  const pascal = generate(32);
  // console.log(pascal);
  // console.log(pascal[rowIndex]);
  return pascal[rowIndex];
};
//--------------------main----------------------------------------------------
console.log(getRow(4));
