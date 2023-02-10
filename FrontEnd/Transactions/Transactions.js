if (!window.sessionStorage.getItem("sessionId")) {
    alert("You do not have access to this page! Please continue to log in or create your own credentials!");
    window.location.href = "../Customer/ManageLogin/Login.html";
};

function navigateToHome() {
    window.location.href = "../Home/CustomerHome.html";
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

async function viewTransactions() {
    // initializing URL varible
    const viewTransactionsURL = "http://127.0.0.1:5000/get/all/transactions";

    // grabbing input from the DOM
    const accountId = document.getElementById("accountTransactionDropDownMenu").value;
    const sessionId = window.sessionStorage.getItem("sessionId")

    // preparing JSON
    viewTransactionsDictionary = {
        'sessionId': sessionId,
        'accountId': accountId
    };

    // preparing request
    let viewTransactionsRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(viewTransactionsDictionary)
    };

    // sending request and awaiting response
    const response = await fetch(viewTransactionsURL, viewTransactionsRequest);

    // handling API response approapriately
    if (response.status === 201) {
        const transactionData = await response.json();
        const transactionList = transactionData.transactionList;
        populateTransactions(transactionList);
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

function populateTransactions(transactionList) {
    let count = 0;
    const transactionTable = document.getElementById("viewTransactionsTable");
    for (transaction in transactionList) {   
        // issue lies within this section when parsing information out     
        const transactionId = Number(String(transactionList[count]).split(", ")[0]);
        const dateTime = String(transactionList[count]).split(", ")[1];
        const transactionType = String(transactionList[count]).split(", ")[2];
        const amount = String(transactionList[count]).split(", ")[4];
        // end of issue
        const row = document.createElement("tr");
        transactionTable.appendChild(row);
        
        const tableData1 = document.createElement("td");
        const square1 = document.createElement("h6");
        square1.className = "form-control-label";
        square1.textContent = `Transaction ID: ${transactionId}`;
        row.appendChild(tableData1);
        tableData1.appendChild(square1);

        const tableData2 = document.createElement("td");
        const square2 = document.createElement("h6");
        square2.className = "form-control-label";
        square2.textContent = `Date and time of transaction: ${dateTime}`;
        row.appendChild(tableData2);
        tableData2.appendChild(square2);

        const tableData3 = document.createElement("td");
        const square3 = document.createElement("h6");
        square3.className = "form-control-label";
        square3.textContent = `Transaction type: ${transactionType}`;
        row.appendChild(tableData3);
        tableData3.appendChild(square3);

        const tableData4 = document.createElement("td");
        const square4 = document.createElement("h6");
        square4.className = "form-control-label";
        square4.textContent = `Transacion amount: ${amount}}`;
        row.appendChild(tableData4);
        tableData4.appendChild(square4);

        count = count + 1;
        };
};

async function getTransactionsAccountsDropDown(){

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
        const accountList = accountData.accountList;
        populateTransactionAccountsDropdown(accountList);
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
        if (apiResponse.message === "Session has expired, please log in!") {
            doLogout();
        };
        resetInputs();
    } else {
        alert("Something went horribly wrong...")
        resetInputs();
    };
};

function populateTransactionAccountsDropdown(accountList) {
    let count = 0;
    const accountTransactionDropDownMenu = document.getElementById("accountTransactionDropDownMenu");
    accountTransactionDropDownMenu.innerHTML = "";
    for (account in accountList) {        
        const accountId = Number(accountList[count].split(", ")[0]);
        const account = document.createElement("option");
        account.value = accountId;
        account.innerHTML = accountId;
        accountTransactionDropDownMenu.appendChild(account);
        count = count + 1;
    };
};

function resetInputs() {
    accountTransactionDropdownMenu = document.getElementById("accountDepositDropDownMenu");
    accountTransactionDropdownMenu.value = "";
    accountTransactionDropdownMenu.innerHTML = "";
    initialTransactionOption = document.createElement("option");
    initialTransactionOption.innerHTML = "Please select an account number";
    accountTransactionDropDownMenu.appendChild(initialTransactionOption);
}
