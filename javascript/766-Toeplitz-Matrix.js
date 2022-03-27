// Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

// A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

// Example 1:


// Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
// Output: true
// Explanation:
// In the above grid, the diagonals are:
// "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
// In each diagonal all elements are the same, so the answer is True.
// Example 2:


// Input: matrix = [[1,2],[2,2]]
// Output: false
// Explanation:
// The diagonal "[1, 2]" has different elements.
 

// Constraints:

// m == matrix.length
// n == matrix[i].length
// 1 <= m, n <= 20
// 0 <= matrix[i][j] <= 99


const randint=(max)=>{
  return Math.floor(Math.random()*max)
}
const gen_arr=()=>{
  let res=[]
  let len=randint(50)+1
  for(let i=0;i<len;i++){
    res.push(randint(100))
  }
  return res;
}
const isToeplitzMatrix=(matrix)=>{
  for(let row=0;row<matrix.length;row++){
    let temp_row=row;
    let col=0
    let first=matrix[row][col]
    console.log(first)
    while(temp_row<matrix.length&&col<matrix[0].length){
      console.log(matrix[temp_row][col])
      if(matrix[temp_row][col]!==first){return false}
      temp_row+=1
      col+=1
    }
  }
  for(let col=0;col<matrix[0].length;col++){
    let temp_col=col;
    let row=0;
    let first=matrix[row][col]
    while(temp_col<matrix[0].length&&row<matrix.length){
      console.log(matrix[row][temp_col])
      if(matrix[row][temp_col]!==first){return false}
      temp_col+=1;
      row+=1;
    }
  }
  return true;
}
  //--------------------main----------------------------------------------------

isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
