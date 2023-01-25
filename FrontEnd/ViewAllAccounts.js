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
        count = count + 1;
    };
};
