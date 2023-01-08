Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


using System;
using System.Collections.Generic;
namespace leetcode
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            int[] list = genArr();

            int[] temp = new int[] { 3,2,4};
            Console.WriteLine( TwoSum(temp, 6));
            
        }
        public  static int[] TwoSum(int[] nums, int target)
        {
            int half = target / 2;
            Console.WriteLine(half);
            int count = 0;
            Dictionary<int, int> dic = new Dictionary<int, int> { };
            int[] res = new int[20];
            int pos = 0;
            for(int i = 0; i < nums.Length;i++)
            {
                if (dic.ContainsKey(target - nums[i]))
                {
                    res[0] = dic[target - nums[i]];
                    res[1] = i;
                    return res;
                }
                if (!dic.ContainsKey(nums[i])) {
                    dic.Add(nums[i], i);
                }
                
            }
            if (count == 2)
            {
                
                for(int i = 0; i < nums.Length; i++)
                {
                    if (nums[i] == half) { res[pos] = i;pos++; }
                }
                return res;
            }
            
            
            foreach(KeyValuePair<int,int>kvp in dic)
            {
                
                if (dic.ContainsKey(target - kvp.Key)&&kvp.Key!=half)
                {
                    Console.WriteLine("pos is: "+pos );
                    res[pos] = kvp.Value;
                    pos++;
                    
                }
            }
            return res;
        }
        public static int [] genArr()
        {
            Random rand = new Random();
            int size = rand.Next(100);
            int[] res = new int[size];
            for(int i = 0; i < size; i++)
            {
                res[i] = rand.Next(1000);
            }
            return res;
        }
        


    }

    }
