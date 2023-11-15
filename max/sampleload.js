var characters = ["samus", "pikachu", "falcon", "ness", "luigi", "mario", "dk", "kirby", "jiggypuff", "link", "fox", "yoshi"]
var samples = ["A.wav","B.wav", "Start.wav", "R.wav", "L.wav", "Z.wav"]

inlets = 1;
outlets = samples.length;
function msg_int(msg){
	for(var i = 0; i<samples.length; i++){
		outlet(i, "open", "./samples/"+characters[msg]+"/"+samples[i])
		}
	}