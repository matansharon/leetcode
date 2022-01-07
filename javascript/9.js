// Given an integer x, return true if x is palindrome integer.

// An integer is a palindrome when it reads the same backward as forward.

// For example, 121 is a palindrome while 123 is not.
 

// Example 1:

// Input: x = 121
// Output: true
// Explanation: 121 reads as 121 from left to right and from right to left.
// Example 2:

// Input: x = -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// Example 3:

// Input: x = 10
// Output: false
// Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

// Constraints:

// -231 <= x <= 231 - 1
 

// Follow up: Could you solve it without converting the integer to a string?


/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = function(x) {
    
    let max = 2 ** 31;
    let min = -((2 ** 31) - 1);
    let x_str = (x + '');
    let x_num = x_str.length;
    
    if (x_num < min || x_num > max) {
        console.log('validate fail');
        return;
    }

    if (x_num < 0) {
        console.log('validate fail');
        return;
    }

    let backword_x = '';
    for (let i = (x_num-1); i >= 0; i--) {
        backword_x = backword_x + x_str.charAt(i);
    }
    
    return x == Number(backword_x);
    
};
