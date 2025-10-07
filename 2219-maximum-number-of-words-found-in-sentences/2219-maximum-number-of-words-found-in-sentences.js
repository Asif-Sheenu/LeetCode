
var mostWordsFound = function(sentences) {
    let maxy = 0;
    for (let i of sentences) {
        let s = i.split(" ").length; 
        maxy = Math.max(maxy, s);    
    }
    return maxy;
};