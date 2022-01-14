// Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

// Example 1:


// Input: head = [1,1,2]
// Output: [1,2]
// Example 2:


// Input: head = [1,1,2,3,3]
// Output: [1,2,3]
 

// Constraints:

// The number of nodes in the list is in the range [0, 300].
// -100 <= Node.val <= 100
// The list is guaranteed to be sorted in ascending order.


const randint = (val) => {
  return Math.floor(Math.random() * val);
};

// Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val;
  this.next = next;
}
const random_list = () => {
  const head = new ListNode(-100);
  let next = head;
  let curr_val = -100;
  let len1 = randint(300);

  for (let i = 0; i < len1; i++) {
    const chance = Math.random();

    const node = new ListNode(curr_val);
    if (chance > 0.5) {
      curr_val++;
    }
    next.next = node;
    next = next.next;
  }
  return head;
};
const print_list = (head) => {
  let next = head;
  let arr = [];
  while (next) {
    arr.push(next.val);
    next = next.next;
  }
  console.log(arr);
};
/*
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
  if (!head) {
    return null;
  }
  let curr = head;
  let set = new Set();
  while (curr) {
    set.add(curr.val);
    curr = curr.next;
  }
  let arr = Array.from(set);
  let res = new ListNode(arr[0]);
  let next = res;
  for (let i = 1; i < arr.length; i++) {
    let temp = new ListNode(arr[i]);
    next.next = temp;
    next = next.next;
  }
  return res;
};

//--------------------main----------------------------------------------------
let head = random_list();
// console.log(head);
print_list(head);
head = deleteDuplicates(head);
print_list(head);
