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
        const transactionList = transactionData.tansactionList;
        window.location.href = "Transactions.html"
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
    transactionTable.innerHTML = "";
    for (transaction in transactionList) {        
        const transactionId = Number(transactionList[count].split(", ")[0]);
        const dateTime = String(transactionList[count].split(", ")[1]);
        const transactionType = String(transactionList[count].split(", ")[2]);
        const amount = String(transactionList[count].split(", ")[4]);
        const row = document.createElement("tr");
        accountTable.appendChild(row);
        
        const square1 = document.createElement("td");
        square1.textContent = `Transaction ID: ${transactionId}`;
        row.appendChild(square1);

        const square2 = document.createElement("td");
        square2.textContent = `Date and time of transaction: ${dateTime}`;
        row.appendChild(square2);

        const square3 = document.createElement("td");
        square2.textContent = `Transaction type: ${transactionType}`;
        row.appendChild(square3);

        const square4 = document.createElement("td");
        square2.textContent = `Transacion amount: ${amount}}`;
        row.appendChild(square4);

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
        const accountList = accountData.accountList
        populateTransactionAccountsDropdown(accountList);
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
