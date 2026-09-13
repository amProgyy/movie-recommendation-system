const signupForm = document.getElementById("sign-up");
const message = document.getElementById("message");
console.log("Hello, World!");
signupForm.addEventListener("submit", async function (event) {
    event.preventDefault()
    
    const username = document.getElementById("name").value;
    console.log(username);
    const email = document.getElementById("email").value;
    const password = document.getElementById("pswd").value;
    
    try {
        const response = await fetch("http://127.0.0.1:8000/auth/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                email: email,
                password: password
            })
        });

        const data = await response.json();

        if (response.ok) {
            message.textContent = data.message || "Registration successful!";
            message.style.color = "green";

            signupForm.reset();

            setTimeout(() => { window.location.href = "/sign_in"; }, 1000);
            
        } else {
            message.textContent = data.detail || "Registration failed.";
            message.style.color = "red";
        }

    } catch (error) {
        console.error("Error:", error);

        message.textContent =
            "Cannot connect to the server. Make sure FastAPI is running.";
        message.style.color = "red";
    }
});