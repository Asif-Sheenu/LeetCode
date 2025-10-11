

var isThree = function (n) {
    // let i =0
    count = 0
    for (let i = 1; n >= i; i++) {
        if (n % i == 0)
            count++
    }
    if (count == 3) {
        return true
    } else { return false }
    return count
};