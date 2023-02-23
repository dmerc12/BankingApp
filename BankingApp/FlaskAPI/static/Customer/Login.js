async function doLogin() {
    // initializing URL variable
    const loginURL = "http://127.0.0.1:5000/login/now"

    // grabbing inputs from DOM
    const email = document.getElementById("emailInput").value;
    const password = document.getElementById("passwordInput").value;

    // preparing JSON
    let loginJSON = {
        "email": email,
        "password": password
    }

    // preparing login request
    let loginInfo = {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(loginJSON)
    };

    // sending request and awaiting API response
    let response = await fetch(loginURL, loginInfo);

    // handling API response appropriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        window.sessionStorage.setItem("sessionId", apiResponse.sessionId);
        alert("Successful login attempt, please continue!")
        {{ redirect( url_for('customer_routes.home'))}};
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(apiResponse.message);
        {{ redirect( url_for('customer_routes.home'))}};
    } else {
        alert("Something went horribly wrong if I'm visible...");
    };
};