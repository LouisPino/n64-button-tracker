var characters = ["Samus", "Pikachu", "Captain-Falcon", "Ness", "Luigi", "Mario", "Donkey-Kong", "Kirby", "Jigglypuff", "Link", "Fox", "Yoshi"]
var samples = ["A.wav", "A1.wav", "A2.wav", "A3.wav", "B.wav", "Start.wav", "R.wav", "L.wav", "Z.wav", "Mash.wav"]

inlets = 1;
outlets = samples.length;
function bang() {
	for (var i = 0; i < characters.length; i++) {
		for (var j = 0; j < samples.length; j++) {
			outlet(j, "preloadn", i + 2, "/Users/louispino/Code/n64/samples/" + characters[i] + "/" + characters[i] + samples[j])
		}
	}
}