// Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

// If the tree has more than one mode, return them in any order.

// Assume a BST is defined as follows:

// The left subtree of a node contains only nodes with keys less than or equal to the node's key.
// The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
// Both the left and right subtrees must also be binary search trees.
 

// Example 1:


// Input: root = [1,null,2,2]
// Output: [2]
// Example 2:

// Input: root = [0]
// Output: [0]
 

// Constraints:

// The number of nodes in the tree is in the range [1, 104].
// -105 <= Node.val <= 105


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
    // console.log(arr);
    return arr;
  };
  const findMode=(root)=>{
      let map=new Map();
      if(!root){return []}
      const scan=(node)=>{
          if(!node){return;}
          if(map.has(node.val)===false){map.set(node.val,0)}
          else{map.set(node.val,map.get(node.val)+1)}
          scan(node.left);
          scan(node.right)
      }
      scan(root);
    //   console.log(map)
    let max=0
    for([k,v]of map){
        // console.log(k,v)
        if(v>max){max=v}
    }
    let res=[]
    for([k,v] of map){
        if(v===max){res.push(k)}
    }
    return res;
  }
  //--------------------main----------------------------------------------------
  let head = random_Tree();
  findMode(head);
