

async function doLogin() {
    const loginURL = "http://127.0.0.1:5000/login"

    const username = document.getElementById("usernameInput").value;
    const password = document.getElementById("passwordInput").value;

    let loginJSON = {
        "username": username,
        "password": password
    }

    token = null;

    let loginInfo = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(loginJSON)
    }

    let response = await fetch(loginURL, loginInfo);

    if (response.status === 201) {
        const apiResponse = await response.json();
        alert('Successful login, click continue!');
        window.sessionStorage.setItem("token", apiResponse.token);
        window.open("CustotmerHome.html");
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(apiResponse.message);
    } else {
        alert("Something went horribly wrong if I'm visible...");
    }
}

function goToNewCustomer() {
    window.open("NewCustomer.html")
}
