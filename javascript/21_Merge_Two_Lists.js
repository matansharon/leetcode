//   Definition for singly-linked list.
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
  let res = [];
  list1.forEach((el) => {
    res.push(el);
  });
  list2.forEach((el) => {
    res.push(el);
  });
  // console.log(res)
  res.sort(function (a, b) {
    return a - b;
  });
  console.log(res);
  let head_res = new ListNode(res[0]);
  let p1 = head_res;
  res.forEach((el) => {
    let temp = new ListNode(el);
    p1.next = temp;
    p1 = p1.next;
  });
  // console.log(print_list(head_res));
  return head_res;
};

const convert_to_array = function (head) {
  let p1 = head;
  let res = [];
  while (p1) {
    res.push(p1.val);
    p1 = p1.next;
  }
  return res;
};

const print_list = function (head) {
  let p1 = head;
  let res = [];
  while (p1) {
    res.push(p1.val);
    p1 = p1.next;
  }
  return res;
};
//----------------------------------------------------------------
//main
//----------------------------------------------------------------
let head1 = new ListNode(Math.floor(Math.random() * 100));
let head2 = new ListNode(Math.floor(Math.random() * 100));
let next1 = head1;
let next2 = head2;
// console.log(head1,head2);
for (let i = 0; i < 10; i++) {
  let p1 = new ListNode(Math.floor(Math.random() * 100));
  let p2 = new ListNode(Math.floor(Math.random() * 100));
  next1.next = p1;
  next2.next = p2;
  next1 = next1.next;
  next2 = next2.next;
}
let arr1 = convert_to_array(head1);
let arr2 = convert_to_array(head2);
mergeTwoLists(arr1, arr2);

