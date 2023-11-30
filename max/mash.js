inlets = 1;
outlets = 1;

var count = 0;
var last = "B";

function mash(btn){
	if(btn === last){
		count ++
	}else{
		count = 0}
	last = btn;
	post(btn+"\n")
	if(count===4){
		count = 0;
		outlet(0, "bang");
	}

}