

function resetInputs() {
    accountDeleteDropDownMenu = document.getElementById("accountDeleteDropDownMenu");
    accountDeleteDropDownMenu.value = "";
    accountDeleteDropDownMenu.innerHTML = "";
    initialDeleteOption = document.createElement("option");
    initialDeleteOption.innerHTML = "Please select an account number"
    accountDeleteDropDownMenu.appendChild(initialDeleteOption);
};

async function deleteAccount() {
    // initializing URL varible
    const deleteAccountURL = "http://127.0.0.1:5000/delete/account";

    // grabbing input from the DOM
    const deleteAccountId = document.getElementById("accountDeleteDropDownMenu").value;
    const sessionId = window.sessionStorage.getItem("sessionId");

    // preparing JSON
    deleteAccountDictionary = {
        'sessionId': sessionId,
        'accountId': deleteAccountId
    };

    // preparing request
    let deleteRequest = {
        method: "DELETE",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(deleteAccountDictionary)
    };

    // sending request and awaiting response
    const response = await fetch(deleteAccountURL, deleteRequest);

    // handling API response approapriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        alert("This account has been successfully delteted!");
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

async function getDeleteAccountsDropdown(){

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
        populateDeleteAccountsDropdown(accountList);
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

function populateDeleteAccountsDropdown(accountList) {
    let count = 0;
    const accountDeleteDropdownMenu = document.getElementById("accountDeleteDropDownMenu");
    accountDeleteDropdownMenu.innerHTML = "";
    for (account in accountList) {        
        const accountId = Number(accountList[count].split(", ")[0]);
        const accountOption = document.createElement("option");
        accountOption.name = `accountToDelete${accountId}`;
        accountOption.innerHTML = accountId;
        accountDeleteDropdownMenu.appendChild(accountOption);
        count = count + 1;
    };
};
