
var subtractProductAndSum = function(n) {
 let p= n.toString().split("").map(Number).reduce((a,b)=>a+b)
let po= n.toString().split("").map(Number).reduce((a,b)=>a*b)
return po-p
};