// $(document).ready(function() {
    $("#registerForm").submit(function (event) {
        // Prevent the form from submitting traditionally
        event.preventDefault();
        debugger;
        var em = document.getElementById('email').value;
        var nm = document.getElementById('name').value;
        var pswd = document.getElementById('password').value;
        var cpswd = document.getElementById('confirmPassword').value;
        var adr = document.getElementById('address').value;
        var ph = document.getElementById('phone').value;

        var nmpattern = /^[A-Za-z ]+$/;
        var empattern = /^[A-Za-z0-9!&#*]*.@[a-zA-Z]*.[com]*$/;
        var phpattern = /^(6|7|8|9){1}[0-9]{9}$/;
        const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/;

        // if (!nmpattern.test(nm)) {
        //     alert("Invalid name");
        //     return false;
        // }
        // if (!passwordRegex.test(pswd)) {
        //     alert("Invalid Password");
        //     return false;
        // }
        // if (pswd != cpswd) {
        //     alert("Password and confirm password should be the same");
        //     // Remove the line below to prevent form reset
        //     // FormData.reset();
        //     return false;
        // }
        // if (!phpattern.test(ph)) {
        //     alert("Invalid Phone Number");
        //     return false;
        // }
        // if (!empattern.test(em)) {
        //     alert("Invalid email");
        //     return false;
        // }

        $.ajax({
            type: "GET",
            url: "/regdata",
            contentType: "application/json;charset=UTF-8",
            DataType: "json",
            data: {
                'username': nm,
                'email': em,
                'phone': ph,
                'address': adr,
                'password': pswd,
            },
            success: function (response) {
                alert("Registered Successfully");
                // Handle the success response if needed
                console.log(response);
            },
            error: function (error) {
                alert("Registration Failed");
                // Handle the error response if needed
                console.error(error);
            }
        });
    });
// });
