
var differenceOfSum = function (nums) {

let added=0
let addedp=0

    let pui = nums.toString().split("")
    for (let i = 0; i < pui.length; i++) {
        if (pui[i] !== ",") {
            addedp += Number(pui[i]);
        }
    }

    for (let i = 0; i < nums.length; i++) {
        added += nums[i]
    }

let result = added-addedp
return result
};