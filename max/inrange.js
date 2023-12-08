inlets = 1;
outlets = 1

function msg_int(msg){
if (msg == 0){
outlet(0, .333)
}
else if(msg == 127){
outlet(0, 3);
}	
else if(msg < 50){
outlet(0, .5);
}
else if (msg > 90){
outlet(0, 2);
}else{
outlet(0, 1);
}
}