// Given a string licensePlate and an array of strings words, find the shortest completing word in words.

// A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

// For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

// Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.

 

// Example 1:

// Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
// Output: "steps"
// Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
// "step" contains 't' and 'p', but only contains 1 's'.
// "steps" contains 't', 'p', and both 's' characters.
// "stripe" is missing an 's'.
// "stepple" is missing an 's'.
// Since "steps" is the only word containing all the letters, that is the answer.
// Example 2:

// Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
// Output: "pest"
// Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. The answer is "pest" because it is the word that appears earliest of the 3.
 

// Constraints:

// 1 <= licensePlate.length <= 7
// licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
// 1 <= words.length <= 1000
// 1 <= words[i].length <= 15
// words[i] consists of lower case English letters.



const randint=(max)=>{
  return Math.floor(Math.random()*max)
}
const gen_arr=()=>{
  let res=[]
  let len=randint(50)+1
  for(let i=0;i<len;i++){
    res.push(randint(100))
  }
  return res;
}
const convert_to_map=(str)=>{
  let map=new Map();
  let licensePlate_lower=str.toLowerCase();
  
  for(let i=0;i<licensePlate_lower.length;i++){
    let num=licensePlate_lower.charCodeAt(i)
    let ch=licensePlate_lower[i]
    if(num>=97&&num<123){
      if(map.has(ch)){
        let temp=map.get(ch)+1
        map.set(ch,temp)
      }
      else{
        map.set(ch,1)
      }
    }
    

  }
  // console.log(map)
  return map;

}

const compare_maps=(license,word)=>{
  for([key,val]of license){
    if(!word.has(key)){return false}
    else{
      if(word.get(key)!==val){return false}
    }
  }
  return true;
}
const shortestCompletingWord=(licensePlate, words)=>{
  let license_map=convert_to_map(licensePlate);
  
  let same_map=[]
  for(let word of words){
    let map=convert_to_map(word)
    console.log(word,map)
    if(compare_maps(license_map,map)){same_map.push(word)}
  }
  console.log(same_map)
  let min=Number.MAX_VALUE;
  for(let w of same_map){
    if (w.length<min){
      min=w.length;
    }
  }

  let res=''
  console.log(same_map)
  for(let word of same_map){
    if(word.length===min){return word}
  }
  
  

  }



  //--------------------main----------------------------------------------------

console.log(shortestCompletingWord("GrC8950",["measure","other","every","base","according","level","meeting","none","marriage","rest"]))
