
async function doLogin() {
    // initializing URL variable
    const loginURL = "http://127.0.0.1:5000/login"

    // grabbing inputs from DOM
    const username = document.getElementById("usernameInput").value;
    const password = document.getElementById("passwordInput").value;

    // preparing JSON
    let loginJSON = {
        "username": username,
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
        alert('Successful login, click continue!');
        window.sessionStorage.setItem("customerId", apiResponse.customerId);
        window.sessionStorage.setItem("firstName", apiResponse.firstName);
        window.sessionStorage.setItem("lastName", apiResponse.lastName);
        window.sessionStorage.setItem("username", apiResponse.username);
        window.sessionStorage.setItem("password", apiResponse.password);
        window.sessionStorage.setItem("email", apiResponse.email);
        window.sessionStorage.setItem("phoneNumber", apiResponse.phoneNumber);
        window.sessionStorage.setItem("address", apiResponse.address);
        window.location.href = "CustomerHome.html";
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(apiResponse.message);
    } else {
        alert("Something went horribly wrong if I'm visible...");
    };
};

function goToNewCustomer() {
    window.location.href = "NewCustomer.html";
};
