function validateForm() {
            let email = document.getElementById("email").value;
            let mobile = document.getElementById("mobile").value;

            let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/;
            let mobilePattern = /^[0-9]{10}$/;

            if (!emailPattern.test(email)) {
                alert("Please enter a valid Email.");
                return false;
            }
            if (!mobilePattern.test(mobile)) {
                alert("Please enter a valid 10-digit Mobile Number.");
                return false;
            }
            return true;
        } 