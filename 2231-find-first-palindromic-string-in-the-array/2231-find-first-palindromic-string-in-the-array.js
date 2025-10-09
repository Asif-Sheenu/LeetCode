
var firstPalindrome = function(words) {
    const finds = words.find(f => f === f.split("").reverse().join(""));
if (finds == undefined){
    return ""
}
   return finds
         

};