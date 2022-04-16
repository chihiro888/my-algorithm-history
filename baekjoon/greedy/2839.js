var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' ');
var a = parseInt(input[0]);

function solve(N) {
	var M = parseInt(N/5);
	for (var i=M; i>=0; i--) {
		R = N - (i * 5)
		if (R === 0 || R%3 === 0) {
			var kg3 = R/3
			var kg5 = i
			break;
		}
	}
    console.log(isNaN(kg3+kg5) ? -1 : kg3+kg5);
}

solve(a)