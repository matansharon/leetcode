// Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

// Example 1:


// Input: root = [4,2,6,1,3]
// Output: 1
// Example 2:


// Input: root = [1,0,48,null,null,12,49]
// Output: 1
 

// Constraints:

// The number of nodes in the tree is in the range [2, 104].
// 0 <= Node.val <= 105
 

// Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/


const convert_to_array=(root)=>{

    let arr=[]
    const scan=(node)=>{
        if(!node){return;}
        scan(node.left)
        arr.push(node.val)
        scan(node.right)
    }
    scan(root)
    return arr;
}
const getMinimumDifference=(root)=>{
    let arr=convert_to_array(root)
    let res=Number.MAX_VALUE
    for(let i=0;i<arr.length-1;i++){
        if(arr[i+1]-arr[i]<res){res=arr[i+1]-arr[i]}
    }
    return res
}
  //--------------------main----------------------------------------------------
