// Given the roots of two binary trees p and q, write a function to check if they are the same or not.

// Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

// Example 1:


// Input: p = [1,2,3], q = [1,2,3]
// Output: true
// Example 2:


// Input: p = [1,2], q = [1,null,2]
// Output: false
// Example 3:


// Input: p = [1,2,1], q = [1,1,2]
// Output: false
 

// Constraints:

// The number of nodes in both trees is in the range [0, 100].
// -104 <= Node.val <= 104


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
const InorderTraversal = (root) => {
  curr = root;

  let res = [];
  const scan = (node) => {
    if (node === null) {
      return;
    }
    res.push(node.val);
    if (node.left) {
      scan(node.left);
    } else {
      res.push(null);
    }

    if (node.right) {
      scan(node.right);
    } else {
      res.push(null);
    }
  };
  scan(root);
  console.log(res);
  return res;
};
//--------------------------------------------------------------------------------------------------------------------
const isSameTree = (p, q) => {
  let root1 = InorderTraversal(p);
  let root2 = InorderTraversal(q);
  if (root1.length !== root2.length) {
    return false;
  }
  for (let i = 0; i < root1.length; i++) {
    if (root1[i] !== root2[i]) {
      return false;
    }
  }
  return true;
};
//--------------------main----------------------------------------------------
let root1 = random_tree();
let root2 = random_tree();
isSameTree(root1, root2);

// ===InorderTraversal(root));
