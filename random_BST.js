const randint = (val) => {
  return Math.floor(Math.random() * val);
};
class TreeNode {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}
const random_BST = () => {
  let len = randint(40);
  let arr = new Array(randint(len * 2)).fill(null);

  console.log(len);
  arr[1] = randint(50) + 50;

  for (let i = 1; i < len; i++) {
    if (arr[i * 2] === null) {
      arr[i * 2] = arr[i] - randint(10);
    }
    if (arr[i * 2 + 1] === null) {
      arr[i * 2 + 1] = randint(10) + arr[i];
    }
  }
  for (let i = 1; i < len; i++) {
    let temp = arr[i];
    arr[i] = new TreeNode(temp);
  }
  let len1 = arr.length - 1;
  for (let i = 1; i < len1; i++) {
    if (i * 2 <= len1) {
      arr[i].left = arr[i * 2];
    }
    if (i * 2 + 1 <= len1) {
      arr[i].right = arr[i * 2 + 1];
    }
  }
  // console.log(arr);
  return arr[1];
};

//--------------------main----------------------------------------------------
let root = random_BST();
console.log(root);
