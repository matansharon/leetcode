const randint = (val) => {
  return Math.floor(Math.random() * val);
};
class TreeNode {
  constructor(val, left, right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}
const random_tree = () => {
  const root = new TreeNode(randint(100));
  const len = randint(30);
  for (let i = 0; i < len; i++) {
    let curr = root;
    let next = new TreeNode(randint(100));
    let flag = true;
    while (flag) {
      let chance = Math.random();
      if (chance > 0.5) {
        if (!curr.left) {
          curr.left = next;
          flag = false;
        } else {
          curr = curr.left;
        }
      } else {
        if (!curr.right) {
          curr.right = next;
          flag = false;
        } else {
          curr = curr.right;
        }
      }
    }
  }
  // console.log(root);
  return root;
};
var maxDepth = function (node) {
  if (node === undefined || node === null) {
    return 0;
  } else {
    let left = maxDepth(node.left);
    let right = maxDepth(node.right);
    return Math.max(left, right) + 1;
  }
};

//--------------------main----------------------------------------------------
let root1 = random_tree();
console.log(root1);
console.log(maxDepth(root1));
