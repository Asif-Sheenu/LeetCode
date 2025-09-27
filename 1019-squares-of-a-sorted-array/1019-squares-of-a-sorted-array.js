/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let result= 0
   
        result = nums.map((nums=>nums*nums))
    
return(result.sort((a,b)=>a-b))
};