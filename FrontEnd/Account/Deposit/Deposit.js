async function deposit() {
    // initializing URL varible
    const depositURL = "http://127.0.0.1:5000/deposit";

    // grabbing input from the DOM
    const depositAccountId = document.getElementById("accountDepositDropDownMenu").value;
    const depositAmount = document.getElementById("depositAmountInput").value;
    const sessionId = window.sessionStorage.getItem("sessionId");

    // preparing JSON
    depositDictionary = {
        'sessionId': sessionId,
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
        alert(`Your deposit into account ${apiResponse.accountId} was successful and now has a balance of: $ ${apiResponse.balance}`);
        window.location.href = "../Main/ManageAccounts.html";
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

async function getDepositAccountsDropdown(){

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
        populateDepositAccountsDropdown(accountList);
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

function populateDepositAccountsDropdown(accountList) {
    let count = 0;
    const accountDepositDropdownMenu = document.getElementById("accountDepositDropDownMenu");
    accountDepositDropdownMenu.innerHTML = "";
    for (account in accountList) {        
        const accountId = Number(accountList[count].split(", ")[0]);
        const account = document.createElement("option");
        account.value = accountId;
        account.innerHTML = accountId;
        accountDepositDropdownMenu.appendChild(account);
        count = count + 1;
    };
};

function resetInputs() {
    accountDepositDropdownMenu = document.getElementById("accountDepositDropDownMenu");
    accountDepositDropdownMenu.value = "";
    accountDepositDropdownMenu.innerHTML = "";
    initialDepositOption = document.createElement("option");
    initialDepositOption.innerHTML = "Please select an account number"
    accountDepositDropdownMenu.appendChild(initialDepositOption);

    document.getElementById("depositAmountInput").value = "";
};