// Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

// Example 1:


// Input: root = [1,null,2,3]
// Output: [1,3,2]
// Example 2:

// Input: root = []
// Output: []
// Example 3:

// Input: root = [1]
// Output: [1]
 

// Constraints:

// The number of nodes in the tree is in the range [0, 100].
// -100 <= Node.val <= 100
 

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
  console.log(root);
  return root;
};
const inorderTraversal = function (root) {
  let res = [];
  if (!root) {
    return res;
  }

  const inorder = (node) => {
    if (node.left) {
      inorder(node.left);
    }
    res.push(node.val);
    if (node.right) {
      inorder(node.right);
    }
  };
  inorder(root);
  return res;
};

//--------------------main----------------------------------------------------
let root = random_tree();
let arr = inorderTraversal(root);
console.log(arr);


