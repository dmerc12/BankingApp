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

if (!window.sessionStorage.getItem("sessionId")) {
    alert("You do not have access to this page! Please continue to log in or create your own credentials!");
    window.location.href = "Login.html";
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
        window.location.href = "Login.html";
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
        if (apiResponse.message === "Session has expired, please log in!") {
            window.sessionStorage.removeItem("sessionId");
            alert("Goodbye!");
            window.location.href = "Login.html";
        };
    } else {
        alert("Something went horribly wrong...");
        window.sessionStorage.removeItem("sessionId");
        alert("Goodbye!");
        window.location.href = "Login.html";
    };
};

function goHome() {
    window.location.href = "CustomerHome.html";
};

function resetInputs() {
    document.getElementById("startingAmountInput").value = "";
    document.getElementById("depositAccountIdInput").value = "";
    document.getElementById("depositAmountInput").value = "";
    document.getElementById("withdrawAccountIdInput").value = "";
    document.getElementById("withdrawAmountInput").value = "";
    document.getElementById("transferWithdrawIdInput").value = "";
    document.getElementById("transferDepositIdInput").value = "";
    document.getElementById("transferAmountInput").value = "";
    document.getElementById("deleteAccountIdInput").value = "";
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
        resetInputs();
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
        resetInputs();
        if (apiResponse.message === "Session has expired, please log in!") {
            doLogout();
        };
    } else {
        alert("Something went horribly wrong...")
        resetInputs();
    };
}; 

async function viewAllAccounts() {

    // initializing URL varible
    const viewAllAccountsURL = "http://127.0.0.1:5000/get/all/accounts";

    // grabbing customer ID from the browser and DOM
    const sessionId = window.sessionStorage.getItem("sessionId");

    // preparing JSON
    viewAccountsDictionary = {
        'sessionId': sessionId
    };

    // preparing request
    let viewAccountsRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(viewAccountsDictionary)
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
        if (apiResponse.message === "Session has expired, please log in!") {
            doLogout();
        };
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
        
        const tableData1 = document.createElement("td");
        const square1 = document.createElement("h3");
        square1.textContent = `Account number: ${accountId}`;
        row.appendChild(tableData1);
        tableData1.appendChild(square1);

        const tableData2 = document.createElement("td");
        const square2 = document.createElement("h3");
        square2.textContent = `Balance: $${balance}`;
        row.appendChild(tableData2);
        tableData2.appendChild(square2);

        const tableData3 = document.createElement("td");
        const square3 = document.createElement("button");
        square3.textContent = "View associated transactions";
        square3.id = `viewTransaction${accountId}`;
        square3.className = 'btn';
        square3.addEventListener('onclick', viewAssociatedTransactions(accountId));
        row.appendChild(tableData3);
        tableData3.appendChild(square3)
        count = count + 1;
    };
};

function viewAssociatedTransactions(accountId) {
    // window.sessionStorage.setItem("accountId", accountId);
    // window.location.href = "Transactions.html";
};

async function deposit() {
    // initializing URL varible
    const depositURL = "http://127.0.0.1:5000/deposit";

    // grabbing input from the DOM
    const depositAccountId = document.getElementById("depositAccountIdInput").value;
    const depositAmount = document.getElementById("depositAmountInput").value;

    // preparing JSON
    depositDictionary = {
        'accountId': depositAccountId,
        'depositAmount': depositAmount
    };

    // preparing request
    let depositRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(depositDictionary)
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
    withdrawDictionary = {
        'accountId': withdrawAccountId,
        'withdrawAmount': withdrawAmount
    };

    // preparing request
    let withdrawRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(withdrawDictionary)
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
    transferDictionary = {
        'withdrawAccountId': transferWithdrawAccountId,
        'depositAccountId': transferDepositAccountId,
        'transferAmount': transferAmount
    };

    // preparing request
    let transferRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(transferDictionary)
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
    const deleteAccountId = document.getElementById("deleteAccountIdInput").value;

    // preparing JSON
    deleteAccountDictionary = {
        'accountId': deleteAccountId
    };

    // preparing request
    let deleteRequest = {
        method: "DELETE",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(deleteAccountDitionary)
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
