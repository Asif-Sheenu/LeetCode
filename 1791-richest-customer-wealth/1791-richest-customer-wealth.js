/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
  let result = 0
  for(let i of accounts){
    let sum = i.reduce((a,b) => a+b)
    if(result < sum){
        result = sum
    }
  }  return result
};