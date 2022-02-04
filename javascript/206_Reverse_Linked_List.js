// Given the head of a singly linked list, reverse the list, and return the reversed list.

 

// Example 1:


// Input: head = [1,2,3,4,5]
// Output: [5,4,3,2,1]
// Example 2:


// Input: head = [1,2]
// Output: [2,1]
// Example 3:

// Input: head = []
// Output: []
 

// Constraints:

// The number of nodes in the list is the range [0, 5000].
// -5000 <= Node.val <= 5000
 

// Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?


/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const convert_to_list = (head) => {
  let res = [];
  if (head === null) {
    console.log([]);
    return;
  }
  let curr = head;
  while (curr) {
    res.push(curr.val);
    curr = curr.next;
  }
  return res;
    
};

const reverseList = (head) => {
  if (head === null) {
    return null;
  }
  let arr = convert_to_list(head);
  let res = new ListNode(arr[arr.length - 1]);
  let curr = res;
  for (let i = arr.length - 2; i > -1; i--) {
    curr.next = new ListNode(arr[i]);
    curr = curr.next;
  }
  return res;
};
