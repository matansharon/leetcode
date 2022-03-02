// Given the head of a singly linked list, return true if it is a palindrome.

 

// Example 1:


// Input: head = [1,2,2,1]
// Output: true
// Example 2:


// Input: head = [1,2]
// Output: false
 

// Constraints:

// The number of nodes in the list is in the range [1, 105].
// 0 <= Node.val <= 9
 

// Follow up: Could you do it in O(n) time and O(1) space?

const randint = (val) => {
  return Math.floor(Math.random() * val);
};
class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}
const random_list = () => {
  let len = randint(100);
  let head = new ListNode(randint(100));
  let curr = head;
  for (let i = 0; i < len; i++) {
    curr.next = new ListNode(randint(100));
    curr = curr.next;
  }
  return head;
};
const convert_list_to_array = (head) => {
  let res = [];
  let curr = head;
  while (curr) {
    res.push(curr.val);
    curr = curr.next;
  }
  // console.log(res);
  return res;
};
const isPalindrome = (head) => {
  let arr = convert_list_to_array(head);
  // console.log(arr);
  if (arr.length === 1) {
    return true;
  }
  if (arr.length === 2) {
    if (arr[0] === arr[1]) {
      return true;
    } else {
      return false;
    }
  }
  // console.log(arr)
  let low = 0;
  let high = arr.length - 1;
  while (low < high) {
    if (arr[low] !== arr[high]) {
      return false;
    }
    low++;
    high--;
  }
  return true;
};
//--------------------main----------------------------------------------------
let head = random_list();
console.log(convert_list_to_array(head));
console.log(isPalindrome());
