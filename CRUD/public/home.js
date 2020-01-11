var xhttp;
function reqListener () {
	console.log('123')
	console.log('xhttp', xhttp)
	console.log(xhttp.responseText);
	dataDiv.innerHTML += xhttp.responseText;
}

function myScript(){
	var dataDiv = document.getElementById('data')
	var dataStr =  "<table style='border:solid; border-collapse:collapse; width:60%'>\
					  <tr>\
					    <th>ID</th>\
					    <th>Name</th>\
					    <th>Age</th>\
					    <th>Gender</th>\
					    <th>Branch</th>\
					    <th>TimeStamp</th>\
					    <th>Update</th>\
					    <th>Delete</th>\
					  </tr>\
					</table>"
	dataDiv.innerHTML = dataStr


	xhttp = new XMLHttpRequest();
	

	xhttp.open("GET","http://127.0.0.1:8000/students");
	xhttp.send();
	xhttp.addEventListener("loadend", reqListener)
	//console.log('here1')
	//console.log(xhttp.responseText)
	// xhttp.onreadystatechange = function(){
	// 	if(xhttp.readyState === XMLHttpRequest.DONE && xhttp.status== 200) {
	// 		console.log('response')
	// 	    console.log(xhttp.responseText);
	// 	  }
	// 	// console.log(xhttp.responseText)
	// };
	dataDiv.innerHTML += xhttp.responseText;

}




function showForm(){
	var form = document.getElementById('form')
	var btn = document.getElementById('addBtn')

	if(btn.value=='Hide'){	
		form.style.display='none'
		btn.value = 'Add'
	}
	else{
		form.style.display='block'
		btn.value = 'Hide'
	}
}