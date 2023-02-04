if (!window.sessionStorage.getItem("sessionId")) {
    alert("You do not have access to this page! Please continue to log in or create your own credentials!");
    window.location.href = "../../Customer/ManageLogin/Login.html";
};

async function createAccount() {
    // initializing URL varible
    const createAccountURL = "http://127.0.0.1:5000/create/account";

    // grabbing input from the DOM
    const balance = document.getElementById("startingAmountInput").value;
    const sessionId = window.sessionStorage.getItem("sessionId");

    // preparing JSON
    newAccountJSON = {
        'sessionId': sessionId,
        'balance': balance
    };

    // preparing request
    let newAccountRequest = {
        method: "POST",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(newAccountJSON)
    };

    // sending request and awaiting response
    const response = await fetch(createAccountURL, newAccountRequest);

    // handling API response approapriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        alert(`Account successfully created with a generated account number of ${apiResponse.accountId} with a balance of $${apiResponse.balance}`);
        window.location.href = "../Main/ManageAccounts.html";
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
        resetInputs();
        if (apiResponse.message === "Session has expired, please log in!") {
            doLogout();
        };
    } else {
        alert("Something went horribly wrong...");
        resetInputs();
    };
}; 

function resetInputs() {
    document.getElementById("startingAmountInput").value = "";
};

function navigateToManageAccounts() {
    window.location.href = "../Account/Main/ManageAccounts.html";
};

async function doLogout() {
    // initializing URL varible
    logoutURL = "http://127.0.0.1:5000/logout"

    // grabbing input from the DOM
    const sessionId = window.sessionStorage.getItem("sessionId");

    // preparing JSON
    logoutDictionary = {
        "sessionId": sessionId
    };

    // preparing request
    let logoutRequest = {
        method: "DELETE",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(logoutDictionary)
    };

    // sending request and awaiting response
    const response = await fetch(logoutURL, logoutRequest)

    // handling API response approapriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        window.sessionStorage.removeItem("sessionId");
        alert("Goodbye!");
        window.location.href = "../../Customer/ManageLogin/Login.html";
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
        if (apiResponse.message === "Session has expired, please log in!") {
            window.sessionStorage.removeItem("sessionId");
            alert("Goodbye!");
            window.location.href = "../../Customer/ManageLogin/Login.html";
        };
    } else {
        alert("Something went horribly wrong...");
        window.sessionStorage.removeItem("sessionId");
        alert("Goodbye!");
        window.location.href = "../../Customer/ManageLogin/Login.html";
    };
};