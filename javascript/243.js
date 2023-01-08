// Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

// Example 1:

// Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
// Output: 3
// Example 2:

// Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
// Output: 1
 

// Constraints:

// 1 <= wordsDict.length <= 3 * 104
// 1 <= wordsDict[i].length <= 10
// wordsDict[i] consists of lowercase English letters.
// word1 and word2 are in wordsDict.
// word1 != word2


const randint = (val) => {
  return Math.floor(Math.random() * val);
};
const random_word = () => {
  const numbers = "1234567890";
  let len = randint(10);
  let res = numbers[randint(numbers.length - 1)];
  for (let i = 0; i < len; i++) {
    res += numbers[randint(numbers.length)];
  }
  return res;
};
const shortestDistance = (wordsDict, word1, word2) => {
  let res = Number.MAX_VALUE;
  let arr1 = [];
  let arr2 = [];
  for (let i = 0; i < wordsDict.length; i++) {
    if (wordsDict[i] === word1) {
      arr1.push(i);
    }
    if (wordsDict[i] === word2) {
      arr2.push(i);
    }
  }
  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr2.length; j++) {
      temp = Math.abs(arr1[i] - arr2[j]);
      if (temp < res) {
        res = temp;
      }
    }
  }
  console.log(res);
  return res;
};
//--------------------main----------------------------------------------------
shortestDistance(["a", "c", "a", "b"], "a", "b");
