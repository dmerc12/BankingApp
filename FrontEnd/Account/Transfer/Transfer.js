async function transfer() {
    // initializing URL varible
    const transferURL = "http://127.0.0.1:5000/transfer";

    // grabbing input from the DOM
    const transferWithdrawAccountId = document.getElementById("accountTransferWithdrawDropDownMenu").value;
    const transferDepositAccountId = document.getElementById("accountTransferDepositDropDownMenu").value;
    const transferAmount = document.getElementById("transferAmountInput").value;
    const sessionId = window.sessionStorage.getItem("sessionId");

    // preparing JSON
    transferDictionary = {
        'sessionId': sessionId,    
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
        alert(`Your transfer of $${transferAmount} from account ${transferWithdrawAccountId} into account ${transferDepositAccountId} was successful!`);
        window.location.href = "../ManageAccounts.html";
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

async function getTransferDepositAccountsDropdown(){

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
        populateTransferDepositAccountsDropdown(accountList);
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

function populateTransferDepositAccountsDropdown(accountList) {
    let count = 0;
    const accountTransferDepositDropdownMenu = document.getElementById("accountTransferDepositDropDownMenu");
    accountTransferDepositDropdownMenu.innerHTML = "";
    for (account in accountList) {        
        const accountId = Number(accountList[count].split(", ")[0]);
        const account = document.createElement("option");
        account.value = accountId;
        account.innerHTML = accountId;
        accountTransferDepositDropdownMenu.appendChild(account);
        count = count + 1;
    };
};

async function getTransferWithdrawAccountsDropdown(){

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
        populateTransferWithdrawAccountsDropdown(accountList);
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

function populateTransferWithdrawAccountsDropdown(accountList) {
    let count = 0;
    const accountTransferWithdrawDropdownMenu = document.getElementById("accountTransferWithdrawDropDownMenu");
    accountTransferWithdrawDropdownMenu.innerHTML = "";
    for (account in accountList) {        
        const accountId = Number(accountList[count].split(", ")[0]);
        const account = document.createElement("option");
        account.value = accountId;
        account.innerHTML = accountId;
        accountTransferWithdrawDropdownMenu.appendChild(account);
        count = count + 1;
    };
};

function resetInputs() {
    accountTransferWithdrawDropDownMenu = document.getElementById("accountTransferWithdrawDropDownMenu");
    accountTransferWithdrawDropDownMenu.value = "";
    accountTransferWithdrawDropDownMenu.innerHTML = "";
    initialTransferWithdrawOption = document.createElement("option");
    initialTransferWithdrawOption.innerHTML = "Please select an account number"
    accountTransferWithdrawDropDownMenu.appendChild(initialTransferWithdrawOption);

    accountTransferDepositDropDownMenu = document.getElementById("accountTransferDepositDropDownMenu");
    accountTransferDepositDropDownMenu.value = "";
    accountTransferDepositDropDownMenu.innerHTML = "";
    initialTransferDepositOption = document.createElement("option");
    initialTransferDepositOption.innerHTML = "Please select an account number"
    accountTransferDepositDropDownMenu.appendChild(initialTransferDepositOption);

    document.getElementById("transferAmountInput").value = "";
};