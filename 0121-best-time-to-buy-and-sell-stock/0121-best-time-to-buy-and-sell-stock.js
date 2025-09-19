
var maxProfit = function(prices) {
        let buy = prices[0]
    let profit = 0
    for(sell of prices){
        if(sell<buy){
            buy = sell
        }else{
            if(profit < sell-buy){
                profit = sell-buy
            }
        }
    }
    return profit
};