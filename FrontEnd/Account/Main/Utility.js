if (!window.sessionStorage.getItem("sessionId")) {
    alert("You do not have access to this page! Please continue to log in or create your own credentials!");
    window.location.href = "../../Customer/ManageLogin/Login.html";
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

function navigateToCreateAnAccount() {
    window.location.href = "../Create/CreateAccount.html";
};

function navigateToViewAllAccounts() {
    window.location.href = "../ViewAll/ViewAllAccounts.html";
};

function navigateToDepositIntoAnAccount() {
    window.location.href = "../Deposit/Deposit.html";
};

function navigateToWithdrawFromAnAccount() {
    window.location.href = "../Withdraw/Withdraw.html";
};

function navigateToTransferBetweenAccounts() {
    window.location.href = "../Transfer/Transfer.html";
};

function navigateToDeleteAnAccount() {
    window.location.href = "../Delete/DeleteAccount.html";
};
