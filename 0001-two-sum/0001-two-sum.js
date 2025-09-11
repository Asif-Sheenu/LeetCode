/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    for (let i=0; nums.length>i;i++){
        for (let j =i+1 ;j<nums.length;j++){
             if (nums[i]+nums[j]===target)
    return[i,j]
        }
    }
   

};