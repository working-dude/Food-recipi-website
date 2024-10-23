$("#btn_accessaccount").click(function(event){
    event.preventDefault(); // Prevent the default behavior of the button

    debugger;
    var em=document.getElementById('email').value;
    var pswd=document.getElementById('password').value;

    var empattern=/^[A-Za-z0-9!&#*]*.@[a-zA-Z]*.[com]*$/;
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/;

    // if(!empattern.test(em))
    // {
    //     alert("Invalid email");
    //     return false;
    // }
    
    // if(!passwordRegex.test(pswd))
    // {
    //     alert("Invalid Password");
    //     return false;
    // }

    $.ajax({
    type:"GET",
    url:"/logdata",
    contentType:"application/json;charset=UTF-8",
    DataType:"json",
    data:{
        'email':em,
        'password':pswd,
    },
    success: function (result) {
        // Handle the success result if needed
        console.log(result);
        if(result=="Success")
			{
				alert('Logged in Successfully');
				window.location="index";
			}
			else{
				alert('Credentials not found');
			}
    },
    error: function (error) {
        // Handle the error response if needed
        console.error(error);
        alert('Error');
    }
    });
    
});
