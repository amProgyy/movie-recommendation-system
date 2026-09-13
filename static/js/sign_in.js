const signinForm = document.getElementById("sign-in");
const message = document.getElementById("message");
signinForm.addEventListener("submit", async function (event) {
    event.preventDefault()
    

    const email = document.getElementById("email").value;
    const password = document.getElementById("pswd").value;
    
    try {
        const response = await fetch("http://127.0.0.1:8000/auth/signin", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        });

        const data = await response.json();
        console.log("Status:", response.status);
        console.log("Response:", data);

        if (response.ok) {
            message.textContent = data.message || "Login successful!";
            message.style.color = "green";

            signinForm.reset();

            setTimeout(() => { window.location.href = "/recommend"; }, 1000);
            
        } else {
            message.textContent = data.detail || "Login failed.";
            message.style.color = "red";
        }

    } catch (error) {
        console.error("Error:", error);

        message.textContent =
            "Cannot connect to the server. Make sure FastAPI is running.";
        message.style.color = "red";
    }
});