var reverse = function(x) {
    let reversed;

    if (x < 0) {
        reversed = Number(Math.abs(x).toString().split("").reverse().join("")) * -1;
    } else {
        reversed = Number(x.toString().split("").reverse().join(""));
    }

    if (reversed < -(2**31) || reversed > 2**31 - 1) {
        return 0;
    }

    return reversed;
};

