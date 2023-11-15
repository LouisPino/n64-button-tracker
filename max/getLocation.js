inlets = 1;
outlets = 1;

function anything() {
	var path = arrayfromargs(messagename, arguments);
		post(path)
	var newPath = path
	outlet(0, newPath);
}