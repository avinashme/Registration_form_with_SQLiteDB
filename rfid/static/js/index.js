<!--JavaScript Validation-->

	    function validation(){
			let fName = document.getElementById('firstName').value;
			let Lname = document.getElementById('lastName').value;
			let emails = document.getElementById('email').value;
			let phonenumber = document.getElementById('phoneNumber').value;
			let gender = document.forms.gender;

			if(fName == "") {
				alert('Please enter your first name.');
				return false;
			}
			if(fName.length < 2 || fName.length>30){
				alert('- First name must be Greater than 2 Character' + '\n' + '  & Less than 50 Character');
				return false;
			}
			if(!isNaN(fName)){
				alert('Only characters are allowed in first name.');
				return false;
			}

			if(Lname == ""){
				alert('Please enter your last name.');
				return false;
			}
			if(Lname.length < 2 || Lname.length>30){
				alert('- Last name must be Greater than 2 Character' + '\n' + '  & Less than 50 Character' );
				return false;
			}
			if(!isNaN(Lname)){
				alert('Only characters are allowed in last name.');
				return false;
			}
			if(emails == ""){
				alert('Please enter your Email name.');
				return false;
			}
			if(emails.indexOf('@')<=0){
				alert('@ Position is Invalid');
				return false;
			}
			if((emails.charAt(emails.length-4) != '.') && (emails.charAt(emails.length-3) != '.')) {
				alert('After @. only 2 or 3 Characters are allowed.');
				return false;
			}
			if(phonenumber == ""){
				alert('Please enter your phone number.');
				return false;
			}
			if(isNaN(phonenumber)){
				alert('Please Enter only number no characters are allowed.');
				return false;
			}
			if(phonenumber.length!=10){
				alert('Mobile number must be of 10 digits.');
				return false;
			}

			for(i=0;i<gender.length;i++){
				if(gender[i].checked == true){
					return true;
				}
				if(i==1){
					alert('Please select the Gender');
					return false;
				}
			}
		}
		function goBack() {
		    window.history.back();
		}
