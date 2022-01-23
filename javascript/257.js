// Given the root of a binary tree, return all root-to-leaf paths in any order.

// A leaf is a node with no children.

 

// Example 1:


// Input: root = [1,2,3,null,5]
// Output: ["1->2->5","1->3"]
// Example 2:

// Input: root = [1]
// Output: ["1"]
 

// Constraints:

// The number of nodes in the tree is in the range [1, 100].
// -100 <= Node.val <= 100


// this is a random generator for a binary tree in javascript

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
const random_Tree = () => {
  let len = randint(10);
  const head = new TreeNode(randint(100));

  for (let i = 0; i < len; i++) {
    curr = head;
    while (curr) {
      if (!curr.left && !curr.right) {
        if (Math.random() > 0.5) {
          curr.right = new TreeNode(randint(100));
        } else {
          curr.left = new TreeNode(randint(100));
        }
        break;
      } else if (curr.right !== null && curr.left === null) {
        curr.left = new TreeNode(randint(100));
        break;
      } else if (curr.right === null && curr.left !== null) {
        curr.right = new TreeNode(randint(100));
        break;
      } else {
        if (curr.left !== null && curr.right !== null) {
          if (Math.random() > 0.5) {
            curr = curr.right;
          } else {
            curr = curr.left;
          }
        }
      }
    }
  }
  return head;
};
const print_tree_inorder = (head) => {
  let arr = [];

  const scan = (node) => {
    if (!node) {
      return;
    }
    if (node) arr.push(node.val);
    scan(node.left);
    scan(node.right);
  };
  scan(head);
  console.log(arr);
};
const binaryTreePaths = (root) => {
  let res = [];

  const scan = (node, path) => {
    if (node) {
      path += node.val.toString();
      if (!node.left && !node.right) {
        res.push(path);
      } else {
        path += "->";
      }
      scan(node.left, path);
      scan(node.right, path);
    }
  };

  scan(root, "");
  return res;
};
//--------------------main----------------------------------------------------
let head = random_Tree();
print_tree_inorder(head);
console.log(binaryTreePaths(head));
