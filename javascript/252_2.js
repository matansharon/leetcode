// Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 

// Example 1:

// Input: intervals = [[0,30],[5,10],[15,20]]
// Output: false
// Example 2:

// Input: intervals = [[7,10],[2,4]]
// Output: true
 

// Constraints:

// 0 <= intervals.length <= 104
// intervals[i].length == 2
// 0 <= starti < endi <= 106


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_arr = () => {
  let arr = [];
  let len = randint(100);
  for (let i = 0; i < len; i++) {
    let start = randint(100);
    let end = start + randint(20);
    arr.push([start, end]);
  }
  return arr;
};
const canAttendMeetings = (meetings) => {
  let map = new Map();
  let arr = meetings.sort((a, b) => {
    return a[0] - b[0];
  });
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i][1] > arr[i + 1][0]) {
      return false;
    }
  }
  return true;
};

//--------------------main----------------------------------------------------
let arr = random_arr();
console.log(arr);
canAttendMeetings(arr);
