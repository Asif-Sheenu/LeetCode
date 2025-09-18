/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
     let ret=[]
    let nw= s.split(" ")
for (i of nw){
    let word=i.split("").reverse().join("")
    console.log (word)


ret.push(word)

}
return (ret.join(" "))
};
