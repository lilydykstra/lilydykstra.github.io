emailjs.init("CFdfqlChUDJ3GoZLN"); // Replace with your Email.js user ID

async function submitForm() {
    // Get form values
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var message = document.getElementById("message").value;

    // Validate form data
    var errors = [];
    if (name.trim() === "") {
        errors.push("Name is required");
    }
    if (email.trim() === "") {
        errors.push("Email is required");
    }
    if (message.trim() === "") {
        errors.push("Message is required");
    }

    // Display errors or submit the form
    var errorsContainer = document.getElementById("errors");
    if (errors.length > 0) {
        errorsContainer.innerHTML = errors.join("<br>");
    } else {
        // Clear any previous errors
        errorsContainer.innerHTML = "";

        // Send form data to Email.js service
        try {
            const response = await emailjs.send("default_service", "template_j2cx8bv", {
                name,
                email,
                message,
            });

            console.log("Email sent successfully!", response);
        } catch (error) {
            console.error("Error sending email:", error);
        }
    }
}

function toggleMenu() {
    const menuIcon = document.querySelector('.menu-icon');
    const navMenu = document.querySelector('.nav-menu');

    menuIcon.classList.toggle('collapsed');
    navMenu.style.display = navMenu.style.display === 'flex' ? 'none' : 'flex';
}