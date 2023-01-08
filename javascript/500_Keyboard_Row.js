// Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

// In the American keyboard:

// the first row consists of the characters "qwertyuiop",
// the second row consists of the characters "asdfghjkl", and
// the third row consists of the characters "zxcvbnm".

 

// Example 1:

// Input: words = ["Hello","Alaska","Dad","Peace"]
// Output: ["Alaska","Dad"]
// Example 2:

// Input: words = ["omk"]
// Output: []
// Example 3:

// Input: words = ["adsdf","sfd"]
// Output: ["adsdf","sfd"]
 

// Constraints:

// 1 <= words.length <= 20
// 1 <= words[i].length <= 100
// words[i] consists of English letters (both lowercase and uppercase). 


const randint=(val)=>{
    return Math.round(Math.random()* val)
}
const findWords=(words)=>{
    rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
    let res=[]
    let array_of_maps=[new Map(),new Map(),new Map()]
    for(let i=0;i<array_of_maps.length;i++){
        for(let j=0;j<rows[i].length;j++){
            array_of_maps[i].set(rows[i][j])
        }
    }
    for(let i=0;i<words.length;i++){
        let first=words[i][0].toLowerCase()
        let temp_map;
        if(array_of_maps[0].has(first)){temp_map=array_of_maps[0]}
        else if(array_of_maps[1].has(first)){temp_map=array_of_maps[1]}
        else if(array_of_maps[2].has(first)){temp_map=array_of_maps[2]}
        let flag=true
        for(let j=0;j<words[i].length;j++){
            if(temp_map.has(words[i][j])===false){flag=false}
        }
        if(flag){res.push(words[i])}
        
    }
    console.log(res)
    return res;
}
//--------------------------main------------------------

findWords(["qwer",'hrthf','ncnc']);
