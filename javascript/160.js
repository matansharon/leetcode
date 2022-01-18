// Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

// For example, the following two linked lists begin to intersect at node c1:


// The test cases are generated such that there are no cycles anywhere in the entire linked structure.

// Note that the linked lists must retain their original structure after the function returns.

// Custom Judge:

// The inputs to the judge are given as follows (your program is not given these inputs):

// intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
// listA - The first linked list.
// listB - The second linked list.
// skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
// skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
// The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

 

// Example 1:


// Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
// Output: Intersected at '8'
// Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
// From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
// Example 2:


// Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
// Output: Intersected at '2'
// Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
// From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
// Example 3:


// Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
// Output: No intersection
// Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
// Explanation: The two lists do not intersect, so return null.
 

// Constraints:

// The number of nodes of listA is in the m.
// The number of nodes of listB is in the n.
// 1 <= m, n <= 3 * 104
// 1 <= Node.val <= 105
// 0 <= skipA < m
// 0 <= skipB < n
// intersectVal is 0 if listA and listB do not intersect.
// intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.


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
  let head1 = new Node(randint(100));
  let head2 = new Node(randint(100));
  let last1;
  let len1 = randint(10);
  let len2 = randint(10);
  curr = head1;
  for (let i = 0; i < len1; i++) {
    curr.next = new Node(randint(100));
    curr = curr.next;
  }
  last1 = curr;
  curr = head2;
  for (let i = 0; i < len2; i++) {
    curr.next = new Node(randint(100));
    curr = curr.next;
  }
  let len3 = randint(10) + 3;
  temp = new Node(randint(100));
  last1.next = temp;
  curr.next = temp;
  curr = curr.next;

  for (let i = 0; i < len3; i++) {
    curr.next = new Node(randint(100));
    curr = curr.next;
  }
  print_list(head1);
  print_list(head2);
  return [head1, head2];
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
var getIntersectionNode = function (headA, headB) {
  let set = new Set();
  curr = headA;
  while (curr) {
    set.add(curr);
    curr = curr.next;
  }
  curr = headB;
  while (curr) {
    if (set.has(curr)) {
      return curr;
    } else {
      curr = curr.next;
    }
  }
  return null;
};

//--------------------main----------------------------------------------------
let arr = random_list();
let head1 = arr[0];
let head2 = arr[1];
/////////////
// print_list(head1);
// print_list(head2);
console.log(getIntersectionNode(head1, head2));
