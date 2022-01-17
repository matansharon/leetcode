// Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

// Example 1:


// Input: root = [1,2,2,3,4,4,3]
// Output: true
// Example 2:


// Input: root = [1,2,2,null,3,null,3]
// Output: false
 

// Constraints:

// The number of nodes in the tree is in the range [1, 1000].
// -100 <= Node.val <= 100
 

// Follow up: Could you solve it both recursively and iteratively?


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
  // console.log(res);
  return res;
};
const PostorderTraversal = (root) => {
  curr = root;

  let res = [];
  const scan = (node) => {
    if (node === null) {
      return;
    }
    res.push(node.val);
    if (node.right) {
      scan(node.right);
    } else {
      res.push(null);
    }
    if (node.left) {
      scan(node.left);
    } else {
      res.push(null);
    }
  };
  scan(root);
  // console.log(res);
  return res;
};

//--------------------------------------------------------------------------------------------------------------------
var isSymmetric = function (root) {
  let root1 = null;
  let root2 = null;
  if (root.left) {
    root1 = InorderTraversal(root.left);
  }
  if (root.right) {
    root2 = PostorderTraversal(root.right);
  }
  if ((root1 && !root2) || (!root1 && root2)) {
    return false;
  }
  if (!root1 && !root2) {
    return true;
  }
  if (root1.length !== root2.length) {
    return false;
  }
  // console.log(root1);
  // console.log(root2);

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
root2 = root1;
console.log(isSymmetric(root1, root2));
