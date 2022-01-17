// Given head, the head of a linked list, determine if the linked list has a cycle in it.

// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

// Return true if there is a cycle in the linked list. Otherwise, return false.

 

// Example 1:


// Input: head = [3,2,0,-4], pos = 1
// Output: true
// Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
// Example 2:


// Input: head = [1,2], pos = 0
// Output: true
// Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
// Example 3:


// Input: head = [1], pos = -1
// Output: false
// Explanation: There is no cycle in the linked list.
 

// Constraints:

// The number of the nodes in the list is in the range [0, 104].
// -105 <= Node.val <= 105
// pos is -1 or a valid index in the linked-list.
 

// Follow up: Can you solve it using O(1) (i.e. constant) memory?


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
class Node {
  constructor(val, next) {
    this.val = val;
    this.next = next;
  }
}
const random_list = () => {
  let arr = [...Array(100).keys()].sort(() => 0.5 - Math.random());
  let head = new Node(arr.pop());
  curr = head;
  while (arr.length > 0) {
    curr.next = new Node(arr.pop());
    curr = curr.next;
  }
  return head;
};
const print_list = (head) => {
  let curr = head;
  let res = [];
  while (curr) {
    res.push(curr.val);
    curr = curr.next;
  }
  console.log(res);
};
var hasCycle = function (head) {
  let set = new Set();
  let curr = head;
  while (curr) {
    if (set.has(curr)) {
      return true;
    } else {
      set.add(curr);
    }
    curr = curr.next;
  }
  return false;
};
//--------------------main----------------------------------------------------
let head = random_list();
// print_list(head)
