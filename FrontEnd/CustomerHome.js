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

if (!window.sessionStorage.getItem("customerId")) {
    alert("You do not have access to this page! Please continue to log in or create your own credentials!");
    window.location.href = "Login.html";
};

function doLogout() {
    window.sessionStorage.removeItem("customerId");
    window.sessionStorage.removeItem("firstName");
    window.sessionStorage.removeItem("lastName");
    window.sessionStorage.removeItem("username");
    window.sessionStorage.removeItem("password");
    window.sessionStorage.removeItem("email");
    window.sessionStorage.removeItem("phoneNumber");
    window.sessionStorage.removeItem("address");
    alert("Goodbye!");
    window.location.href = "Login.html";
;}

function resetInputs() {
    document.getElementById("startingAmountInput").value = "";
    document.getElementById("viewAccountIdInput").value = "";
    document.getElementById("depositAccountIdInput").value = "";
    document.getElementById("depositAmountInput").value = "";
    document.getElementById("withdrawAccountIdInput").value = "";
    document.getElementById("withdrawAmountInput").value = "";
    document.getElementById("transferWithdrawIdInput").value = "";
    document.getElementById("transferDepositIdInput").value = "";
    document.getElementById("transferAmountInput").value = "";
    document.getElementById("delteAccountIdInput").value = "";
    document.getElementById("updatedFirstNameInput").value = "";
    document.getElementById("updatedLastNameInput").value = "";
    document.getElementById("updatedUsernameInput").value = "";
    document.getElementById("updatedPasswordInput").value = "";
    document.getElementById("updatedEmailAddressInput").value = "";
    document.getElementById("updatedPhoneNumberInput").value = "";
    document.getElementById("updatedAddressInput").value = "";
    document.getElementById("viewTransactionsAccountIdInput").value = "";
};

async function createAccount() {
    // initializing URL varible
    const createAccountURL = "http://127.0.0.1:5000/create/account";

    // grabbing input from the DOM
    const balance = document.getElementById("startingAmountInput").value;

    // preparing JSON
    newAccountJSON = {
        'customerId': window.sessionStorage.getItem("customerId"),
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

    // grabbing customer ID from the browser and DOM
    const customerId = window.sessionStorage.getItem("customerId");

    // preparing JSON
    viewAccountsJSON = {
        'customerId': customerId
    };

    // preparing request
    let viewAccountsRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(viewAccountsJSON)
    };

    // sending request and awaiting response
    const response = await fetch(viewAllAccountsURL, viewAccountsRequest);

    // handling API response approapriately
    if (response.status === 201) {
        const accountData = await response.json();
        const accountList = accountData.accountList
        populateAccounts(accountList);
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
    } else {
        alert("Something went horribly wrong...")
    };
};

function populateAccounts(accountList) {
    let count = 0;
    const accountTable = document.getElementById("viewAllAccountsTable");
    accountTable.innerHTML = "";
    for (account in accountList) {        
        const accountId = Number(accountList[count].split(", ")[0]);
        const balance = Number(accountList[count].split(", ")[2]);
        const row = document.createElement("tr");
        accountTable.appendChild(row);
        
        const square1 = document.createElement("td");
        square1.textContent = `Account number: ${accountId}`;
        row.appendChild(square1);

        const square2 = document.createElement("td");
        square2.textContent = `Balance: ${balance}`;
        row.appendChild(square2);

        const square3 = document.createElement("button");
        square3.textContent = "View associated transactions";
        square3.id = `viewTransaction${accountId}`;
        square3.onclick = `viewAssociatedTransactions(${accountId})`
        row.appendChild(square3);
        count = count + 1;
    };
};

function viewAssociatedTransactions(accountId) {
    window.sessionStorage.setItem("accountId", accountId);
    window.location.href = "Transactions.html";
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
    const withdrawURL = "http://127.0.0.1:5000/withdraw";

    // grabbing input from the DOM
    const withdrawAccountId = document.getElementById("withdrawAccountIdInput").value;
    const withdrawAmount = document.getElementById("withdrawAmountInput").value;

    // preparing JSON
    withdrawJSON = {
        'accountId': withdrawAccountId,
        'withdrawAmount': withdrawAmount
    };

    // preparing request
    let withdrawRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(withdrawJSON)
    };

    // sending request and awaiting response
    const response = await fetch(withdrawURL, withdrawRequest);

    // handling API response approapriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        alert(`Your withdrawl was successful and now has a balance of: $ ${apiResponse.balance}`);
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

async function transfer() {
    // initializing URL varible
    const transferURL = "http://127.0.0.1:5000/transfer";

    // grabbing input from the DOM
    const transferWithdrawAccountId = document.getElementById("transferWithdrawIdInput").value;
    const transferDepositAccountId = document.getElementById("transferDepositIdInput").value;
    const transferAmount = document.getElementById("transferAmountInput").value;

    // preparing JSON
    transferJSON = {
        'withdrawAccountId': transferWithdrawAccountId,
        'depositAccountId': transferDepositAccountId,
        'transferAmount': transferAmount
    };

    // preparing request
    let transferRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(transferJSON)
    };

    // sending request and awaiting response
    const response = await fetch(transferURL, transferRequest);

    // handling API response approapriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        alert("Your transfer was successful!");
        resetInputs();
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
        resetInputs();
    } else {
        alert("Something went horribly wrong...")
        resetInputs();
    };
}

async function deleteAccount() {
    // initializing URL varible
    const deleteAccountURL = "http://127.0.0.1:5000/delete/account";

    // grabbing input from the DOM
    const deleteAccountId = document.getElementById("delteAccountIdInput").value;

    // preparing JSON
    deleteAccountJSON = {
        'accountId': deleteAccountId
    };

    // preparing request
    let deleteRequest = {
        method: "DELETE",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(deleteAccountJSON)
    };

    // sending request and awaiting response
    const response = await fetch(deleteAccountURL, deleteRequest);

    // handling API response approapriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        alert("This account has been successfully delteted!");
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

// not tested
async function updateCustomer() {
    // initializing URL varible
    const updateCustomerURL = "http://127.0.0.1:5000/update/customer";

    // grabbing input from the DOM
    const updatedFirstName = document.getElementById("updatedFirstNameInput").value;
    const updatedLastName = document.getElementById("updatedLastNameInput").value;
    const updatedUsername = document.getElementById("updatedUsernameInput").value;
    const updatedPassword = document.getElementById("updatedPasswordInput").value;
    const updatedEmailAddress = document.getElementById("updatedEmailAddressInput").value;
    const updatedPhoneNumber = document.getElementById("updatedPhoneNumberInput").value;
    const updatedAddress = document.getElementById("updatedAddressInput").value;

    // checking for empty inputs to fill in with existing values
    if (updatedFirstName === "") {
        updatedFirstName = window.sessionStorage.getItem("firstName");
    };
    if (updatedLastName === "") {
        updatedLastName = window.sessionStorage.getItem("lastName");
    };
    if (updatedUsername === "") {
        updatedUsername = window.sessionStorage.getItem("username");
    };
    if (updatedPassword === "") {
        updatedPassword = window.sessionStorage.getItem("password");
    };
    if (updatedEmailAddress === "") {
        updatedEmailAddress = window.sessionStorage.getItem("email");
    };
    if (updatedPhoneNumber === "") {
        updatedPhoneNumber = window.sessionStorage.getItem("phoneNumber");
    };
    if (updatedAddress === "") {
        updatedAddress = window.sessionStorage.getItem("address");
    };

    // preparing JSON
    updateCustomerJSON = {
        "customerId": window.sessionStorage.getItem(customerId),
        "firstName": updatedFirstName,
        "lastName": updatedLastName,
        "username": updatedUsername, 
        "password": updatedPassword,
        "email": updatedEmailAddress,
        "phoneNumber": updatedPhoneNumber,
        "address": updatedAddress
    };

    // preparing request
    let updateCustomerRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(updateCustomerJSON)
    };

    // sending request and awaiting response
    const response = await fetch(updateCustomerURL, updateCustomerRequest);

    // handling API response approapriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        alert("Customer information successfully updated!");
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

async function deleteCustomer() {
     // initializing URL varible
     const deleteCustomerURL = "http://127.0.0.1:5000/delete/customer";

     // preparing JSON
     deleteCustomerJSON = {
         'customerId': window.sessionStorage.getItem("customerId")
     };
 
     // preparing request
     let deleteCustomerRequest = {
         method: "DELETE",
         headers: {'Content-Type': "application/json"},
         body: JSON.stringify(deleteCustomerJSON)
     };
 
     // sending request and awaiting response
     const response = await fetch(deleteCustomerURL, deleteCustomerRequest);
 
     // handling API response approapriately
     if (response.status === 201) {
         const apiResponse = await response.json();
         alert("Your information has been successfully delteted!");
         doLogout();
     } else if (response.status === 400) {
         const apiResponse = await response.json();
         alert(`${apiResponse.message}`);
     } else {
         alert("Something went horribly wrong...")
     };
};
