async function withdraw() {
    // initializing URL varible
    const withdrawURL = "http://127.0.0.1:5000/withdraw";

    // grabbing input from the DOM
    const withdrawAccountId = document.getElementById("accountWithdrawDropDownMenu").value;
    const withdrawAmount = document.getElementById("withdrawAmountInput").value;
    const sessionId = window.sessionStorage.getItem("sessionId");

    // preparing JSON
    withdrawDictionary = {
        'sessionId': sessionId,
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
        alert(`Your withdrawl from account ${apiResponse.accountId} was successful and now has a balance of: $ ${apiResponse.balance}`);
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

async function getWithdrawAccountsDropdown(){

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
        populateWithdrawAccountsDropdown(accountList);
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

function populateWithdrawAccountsDropdown(accountList) {
    let count = 0;
    const accountWithdrawDropdownMenu = document.getElementById("accountWithdrawDropDownMenu");
    accountWithdrawDropdownMenu.innerHTML = "";
    for (account in accountList) {        
        const accountId = Number(accountList[count].split(", ")[0]);
        const account = document.createElement("option");
        account.value = accountId;
        account.innerHTML = accountId;
        accountWithdrawDropdownMenu.appendChild(account);
        count = count + 1;
    };
};

function resetInputs() {

    accountWithdrawDropDownMenu = document.getElementById("accountWithdrawDropDownMenu");
    accountWithdrawDropDownMenu.value = "";
    accountWithdrawDropDownMenu.innerHTML = "";
    initialWithdrawOption = document.createElement("option");
    initialWithdrawOption.innerHTML = "Please select an account number"
    accountWithdrawDropDownMenu.appendChild(initialWithdrawOption);

    document.getElementById("withdrawAmountInput").value = "";
};