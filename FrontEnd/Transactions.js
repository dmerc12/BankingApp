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

async function viewTransactions() {
    // initializing URL varible
    const viewTransactionsURL = "http://127.0.0.1:5000/get/all/transactions";

    // grabbing input from the DOM
    const accountId = window.sessionStorage.getItem("accountId");

    // preparing JSON
    viewTransactionsJSON = {
        'accountId': accountId
    };

    // preparing request
    let viewTransactionsRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(viewTransactionsJSON)
    };

    // sending request and awaiting response
    const response = await fetch(viewTransactionsURL, viewTransactionsRequest);

    // handling API response approapriately
    if (response.status === 201) {
        const transactionData = await response.json();
        const transactionList = transactionData.tansactionList;
        populateTransactions(transactionList);
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
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