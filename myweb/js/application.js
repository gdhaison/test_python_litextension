function myRandom(){
	var a = parseInt(document.getElementById("input1").value)
	var b = parseInt(document.getElementById("input2").value) + 1
		c = Math.floor(Math.random() * (b - a)) + a 
	// d = Math.floor(Math.random() * (max - min)) + min
	document.getElementById("result").innerHTML = c
}
