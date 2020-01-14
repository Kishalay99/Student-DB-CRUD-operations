var dataDiv;

function createCORSRequest(method, url){
	var xhr = new XMLHttpRequest();
	if('withCredentials' in xhr){
		xhr.open(method, url, true)
	}
	return xhr
}file:///home/user/Task2/CRUD/public/home.html

function myScript(){
	dataDiv = document.getElementById('data')
	var dataStr =  "<table border='1' style='border-collapse:collapse; margin:10px;'>\
					  <tr>\
					    <th>ID</th>\
					    <th>Name</th>\
					    <th>DOB</th>\
					    <th>Gender</th>\
					    <th>Branch</th>\
					    <th>Created At</th>\
					    <th colspan='2'>Action</th>\
					  </tr>"

	let url = 'http://localhost:8000/students';
	var xhr = createCORSRequest('GET',url);
	   
	xhr.onload = function () {
		console.log(xhr.responseText);
		var json_obj = JSON.parse(xhr.responseText)
		console.log(json_obj)
		let counter=0;
		for(counter;counter<json_obj.length;counter++){
			console.log(json_obj[counter])
			let doby = json_obj[counter].dob.slice(6,10)//<input type="text" value="'+json_obj[counter].gender+'" id="gender'+json_obj[counter].id+'">
			let dobm = json_obj[counter].dob.slice(3,5)
			let dobd = json_obj[counter].dob.slice(0,2)
			dataStr += '<tr>\
							<td><a href="http://127.0.0.1:8000/students/'+json_obj[counter].id+'">'+json_obj[counter].id+'</a></td>\
							<td><input type="text" value="'+json_obj[counter].name+'" id="name'+json_obj[counter].id+'"></td>\
							<td><input type="date" value="'+doby+'-'+dobm+'-'+dobd+'" id="dob'+json_obj[counter].id+'"></td>\
							<td><input type="text" value="'+json_obj[counter].gender+'" id="gender'+json_obj[counter].id+'"></td>\
							<td><select name="branch" id="branch'+json_obj[counter].id+'">\
						<option value="'+json_obj[counter].branch+'">'+json_obj[counter].branch+'</option>\
						<option value="cse">CSE</option>\
						<option value="ise">ISE</option>\
						<option value="mech">MECH</option>\
						<option value="ece">ECE</option>\
					</select></td>\
							<td>'+json_obj[counter].last_updated+'</td>\
							<td><input type=\'button\' value=\'Update\' onclick="updateStudent('+json_obj[counter].id+')" id="upd'+json_obj[counter].id+'"></td>\
							<td><input type=\'button\' value=\'Delete\' onclick="deleteStudent('+json_obj[counter].id+')" id="del'+json_obj[counter].id+'"></td>\
						</tr>'
		}
		dataDiv.innerHTML = dataStr + "</table>";
	}
	xhr.onerror = function() {
		console.log('An error occured')
	}
	xhr.send();
}

function deleteStudent(studentid){
	let url = "http://localhost:8000/students"
	let xhr = createCORSRequest('DELETE', url);
	let data={}
	data.id = studentid;
	let json_str = JSON.stringify(data)
	console.log(json_str)
	xhr.onload = myScript;
	xhr.onerror = function(){
		console.log('failed to delete student')
	}
	xhr.send(json_str)
}

function updateStudent(sid){
	let name = document.getElementById('name'+sid).value
	let dob = document.getElementById('dob'+sid).value
	let gender = document.getElementById('gender'+sid).value
	let branch = document.getElementById('branch'+sid).value
	let data={}

	//dobd = dob.slice(0,2)
	//dobm = dob.slice(3,5)
	//doby = dob.slice(6,10)
	//dob = doby+'-'+dobm+'-'+dobd
	//console.log(dob)

	data.id = sid;
	data.name = name;
	data.dob = dob;
	data.gender = gender;
	data.branch = branch;
	let json_str = JSON.stringify(data)
	console.log(json_str)
	let url = "http://localhost:8000/students"
	let xhr = createCORSRequest('PUT', url);
	xhr.onload = myScript;
	xhr.onerror = function(){
		console.log('failed to update student')
	}
	xhr.send(json_str)
}

function addStudent(){
	let name = document.getElementById('name').value
	let dob = document.getElementById('dob').value
	let gender = document.getElementsByName('gender')
	data={}
	for(let i=0;i<gender.length;i++){
		if (gender[i].checked){
			data.gender = gender[i].value
			break;
		}
	}
	let branch = document.getElementById('branch').value
	console.log(name, dob, data.gender, branch)

	data.name = name
	data.dob = dob
	data.branch = branch

	let url = "http://localhost:8000/students"
	let xhr = createCORSRequest('POST', url);
	let json_str = JSON.stringify(data)
	console.log(json_str)
	xhr.onload = myScript;
	xhr.onerror = function(){
		console.log('failed to add student')
	}
	xhr.send(json_str)
}

function showForm(){
	var form = document.getElementById('form')
	var btn = document.getElementById('addBtn')

	if(btn.value=='Hide'){	
		form.style.display='none'
		btn.value = 'Add '
	}
	else{
		form.style.display='block'
		btn.value = 'Hide'
	}
}