// Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

// Note that the letters wrap around.

// For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 

// Example 1:

// Input: letters = ["c","f","j"], target = "a"
// Output: "c"
// Example 2:

// Input: letters = ["c","f","j"], target = "c"
// Output: "f"
// Example 3:

// Input: letters = ["c","f","j"], target = "d"
// Output: "f"
 

// Constraints:

// 2 <= letters.length <= 104
// letters[i] is a lowercase English letter.
// letters is sorted in non-decreasing order.
// letters contains at least two different characters.
// target is a lowercase English letter.


const nextGreatestLetter=(letters,target)=>{
    if(target===letters[letters.length-1]){return letters[0]}
    let ab="abcdefghijklmnopqrstuvwxyz"
    let map=new Map()
    for(let i=0;i<ab.length;i++){
      map.set(ab[i],i)
    }
    if(map.get(target)>map.get(letters[letters.length-1])){return letters[0]}
    // console.log(map)
    for(ch of letters){
      // console.log(map.get(ch),map.get(target))
      if(map.get(ch)>map.get(target)){return ch}
    }
}
const gen_array=()=>{
  let res=[];
  let ab="abcdefghijklmnopqrstuvwxyz";
  let i=0;
  while(i<ab.length){
    res.push(ab[i])
    i+=Math.floor(Math.random()*10);;
  }
  let target=ab[Math.floor(Math.random()*ab.length)]
  return [res,target];
}
  //--------------------main----------------------------------------------------
let arr=gen_array();
console.log(arr)

console.log(nextGreatestLetter(arr[0],arr[1]))
