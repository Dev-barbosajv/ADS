document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const checkinForm = document.getElementById('checkin-form');

    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            // Add client-side validation for login form
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            if (!username || !password) {
                event.preventDefault();
                alert('Please fill in both username and password.');
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            // Add client-side validation for registration form
            const username = document.getElementById('reg-username').value;
            const password = document.getElementById('reg-password').value;
            if (!username || !password) {
                event.preventDefault();
                alert('Please fill in both username and password.');
            }
        });
    }

    if (checkinForm) {
        checkinForm.addEventListener('submit', function(event) {
            // Add client-side validation for check-in form
            const date = document.getElementById('checkin-date').value;
            const time = document.getElementById('checkin-time').value;
            if (!date || !time) {
                event.preventDefault();
                alert('Please select both date and time for check-in.');
            }
        });
    }
});