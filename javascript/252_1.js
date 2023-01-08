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
const canAttendMeetings=(arr)=>{
  let map=new Map();
  for(let i=0; i<arr.length; i++) {
    for(let start=arr[i][0];start<=arr[i][1]-1;start++) {
      if(map.has(start)){return false;}
      map.set(start)
    }
  }
  // console.log(map)
  return true;
}

//--------------------main----------------------------------------------------
let arr = random_arr();
console.log(arr);
canAttendMeetings(arr);
