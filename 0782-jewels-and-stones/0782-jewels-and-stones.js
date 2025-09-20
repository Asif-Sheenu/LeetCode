var numJewelsInStones = function (jewels, stones) {
   
    let count = 0

    for (let i =0;i<jewels.length;i++) {
        for (let n=0;n<stones.length;n++) {
            if (jewels[i] == stones[n]) {
                count++
            }

        } 
    }
return count
};