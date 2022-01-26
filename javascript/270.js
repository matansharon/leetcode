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

const random_BST_rec = () => {
  let len = randint(30);
  console.log(len);
  let root = new TreeNode(randint(50) + 30);

  const walk = (node) => {
    node.left = new TreeNode(node.val - randint(10));

    node.right = new TreeNode(node.val + randint(10));
    if (Math.random() > 0.5) {
      walk(node.left);
    }
    if (Math.random() > 0.5) {
      walk(node.right);
    }
  };
  walk(root);
  return root;
};
const inorder_traverse = (root) => {
  let arr = [];

  const walk = (node) => {
    if (node === null) {
      return;
    }
    walk(node.left);
    arr.push(node.val);
    walk(node.right);
  };
  walk(root);
  // console.log(arr);
  return arr;
};
const closestValue = (root, target) => {
  let min = Number.MAX_VALUE;
  let res = -1;
  const walk = (node) => {
    if (node === null) {
      return;
    }
    if (Math.abs(node.val - target) < min) {
      min = Math.abs(node.val - target);
      res = node.val;
    }
    walk(node.left);
    walk(node.right);
  };
  walk(root);
  return res;
};
//--------------------main----------------------------------------------------
// let root = random_BST();
// console.log(root);
let root = random_BST_rec();
// console.log(root);
console.log(inorder_traverse(root));
let target = Math.random() * randint(100);
console.log(closestValue(root, target));
