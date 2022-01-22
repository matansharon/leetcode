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
  let len = randint(100);
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
//--------------------main----------------------------------------------------
let head = random_Tree();
print_tree_inorder(head);
