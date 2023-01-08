// Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

// Example 1:


// Input: head = [1,2,6,3,4,5,6], val = 6
// Output: [1,2,3,4,5]
// Example 2:

// Input: head = [], val = 1
// Output: []
// Example 3:

// Input: head = [7,7,7,7], val = 7
// Output: []
 

// Constraints:

// The number of nodes in the list is in the range [0, 104].
// 1 <= Node.val <= 50
// 0 <= val <= 50


/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
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
const removeElements = function (head, val) {
  let arr = convert_to_list(head);
  let clean_arr = [];
  // console.log(arr, val);
    if(arr===undefined){return null}
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== val) {
      clean_arr.push(arr[i]);
    }
  }
  // console.log(clean_arr);
  if (clean_arr.length === 0) {
    return null;
  } else {
    let _head = new ListNode(clean_arr[0]);
    let curr = _head;
    for (let i = 1; i < clean_arr.length; i++) {
      curr.next = new ListNode(clean_arr[i]);
      curr = curr.next;
    }
    return _head;
  }
};
