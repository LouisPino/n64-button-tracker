inlets = 1;
outlets = 2;
function list(list){
var stock = arguments;
stock[stock[2]-1]+=1;
outlet(1,stock[1]);
outlet(0,stock[0]);
}