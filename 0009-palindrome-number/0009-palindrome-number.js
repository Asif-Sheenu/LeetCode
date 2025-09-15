/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  

let nw = x.toString().split("").reverse().join("")
return x.toString()===nw

};