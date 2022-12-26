// grabbing collapsible elements from the DOM
let coll = document.getElementsByClassName("collapsible");
// event listener for collapsible divs
let i;
for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        let content = this.nextElementSibling;
        if (content.style.display === "block") {
        content.style.display = "none";
        } else {
        content.style.display = "block";
        };
    });
};

function doLogout() {
    window.sessionStorage.removeItem("token");
    alert("Goodbye!");
    window.location.href = "Login.html";
;}

function resetInputs() {

};

// needs back end functions build to work
async function viewCustomerId() {
    // initializing URL varible
    const viewCustomeURL = "http://127.0.0.1:5000/get/customer/id";

    // grabbing input from the DOM
    const username = document.getElementById("usernameInput").value;
    const password = document.getElementById("passwordInput").value;

    // preparing JSON
    validationCredentialsJSON = {
        'username': username,
        'password': password
    };

    // preparing request
    let validationRequest = {
        method: "POST",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(validationCredentialsJSON)
    };

    // sending request and awaiting response
    const response = await fetch(viewCustomeURL, validationRequest)

    // handling API response approapriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        alert(`Your assigned customer ID is j${apiResponse.customerId}`);
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
    } else {
        alert("Someting weent horribly wrong...");
    };
};

async function createAccount() {
    // initializing URL varible
    const createAccountURL = "http://127.0.0.1:5000/create/account";

    // grabbing input from the DOM
    const customerId = document.getElementById("createAccountCustomerIdInput").value;
    const balance = document.getElementById("startingAmountInput").value;

    // preparing JSON
    newAccountJSON = {
        'customerId': customerId,
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
        alert(`Account successfully created with a generated account number of ${apiResponse.accountId}`);
        resetInputs();
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
        resetInputs();
    } else {
        alert("Something went horribly wrong...")
        resetInputs();
    };
}; 

async function viewAccountBalance() {
    // initializing URL varible
    const viewAccountBalanceURL = "http://127.0.0.1:5000/get/account";

    // grabbing input from the DOM
    const accountId = document.getElementById("viewAccountIdInput").value;

    // preparing JSON
    getAccountJSON = {
        'accountId': accountId
    };

    // preparing request
    let getAccountRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(getAccountJSON)
    };

    // sending request and awaiting response
    const response = await fetch(viewAccountBalanceURL, getAccountRequest);

    // handling API response approapriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        alert(`The current balance of this account is: $ ${apiResponse.balance}`);
        resetInputs();
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
        resetInputs();
    } else {
        alert("Something went horribly wrong...")
        resetInputs();
    };

};

async function viewAllAccounts() {
    // initializing URL varible
    const viewAllAccountsURL = "http://127.0.0.1:5000/get/all/accounts";

    // grabbing input from the DOM

    // preparing JSON

    // preparing request

    // sending request and awaiting response

    // handling API response approapriately
};

async function deposit() {
    // initializing URL varible
    const depositURL = "http://127.0.0.1:5000/deposit";

    // grabbing input from the DOM
    const depositAccountId = document.getElementById("depositAccountIdInput").value;
    const depositAmount = document.getElementById("depositAmountInput").value;

    // preparing JSON
    depositJSON = {
        'accountId': depositAccountId,
        'depositAmount': depositAmount
    };

    // preparing request
    let depositRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(depositJSON)
    };

    // sending request and awaiting response
    const response = await fetch(depositURL, depositRequest);

    // handling API response approapriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        alert(`Your deposit was successful and now has a balance of: $ ${apiResponse.balance}`);
        resetInputs();
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
        resetInputs();
    } else {
        alert("Something went horribly wrong...")
        resetInputs();
    };
};

async function withdraw() {
    // initializing URL varible
    const depositURL = "http://127.0.0.1:5000/withdraw";

    // grabbing input from the DOM
    const withdrawAccountId = document.getElementById("withdrawAccountIdInput").value;
    const withdrawAmount = document.getElementById("withdrawAmountInput").value;

    // preparing JSON
    withdrawJSON = {
        'accountId': withdrawAccountId,
        'withdrawAmount': withdrawAmount
    };

    // preparing request

    // sending request and awaiting response

    // handling API response approapriately
};

async function transfer() {
    // initializing URL varible

    // grabbing input from the DOM

    // preparing JSON

    // preparing request

    // sending request and awaiting response

    // handling API response approapriately
};

async function viewTransactions() {
    // initializing URL varible

    // grabbing input from the DOM

    // preparing JSON

    // preparing request

    // sending request and awaiting response

    // handling API response approapriately
};

async function deleteAccount() {
    // initializing URL varible

    // grabbing input from the DOM

    // preparing JSON

    // preparing request

    // sending request and awaiting response

    // handling API response approapriately
};

async function updateCustomer() {
    // initializing URL varible

    // grabbing input from the DOM

    // preparing JSON

    // preparing request

    // sending request and awaiting response

    // handling API response approapriately
};

async function deleteCustomer() {
    // initializing URL varible

    // grabbing input from the DOM

    // preparing JSON

    // preparing request

    // sending request and awaiting response

    // handling API response approapriately
};
