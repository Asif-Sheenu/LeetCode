var numberGame = function(nums) {
    let newArr = []
    let arr=nums.length
    let sorted = nums.sort((a,b)=>a-b)
  for (let i = 0 ; i<arr/2;i++){
    let  alice = sorted.shift()
    let bob = sorted.shift()

    newArr.push(bob)
        newArr.push(alice)

  } return newArr;
};
