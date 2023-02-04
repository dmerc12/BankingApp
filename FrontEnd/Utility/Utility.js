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
    window.location.href = "../Customer/ManageLogin/Login.html";
};

function goHome() {
    window.location.href = "../Home/CustomerHome.html";
};

function navigateToManageAccounts() {
    window.location.href = "../Account/Main/ManageAccounts.html";
};

function navigateToManageCustomer() {
    window.location.href = "../Customer/Main/ManageCustomer.html";
};

function navigateToTransactions() {
    window.location.href = "../Transactions/Transactions.html";
};

function navigateToCreateAnAccount() {
    window.location.href = "../Account/Create/CreateAccount.html";
};

function navigateToViewAllAccounts() {
    window.location.href = "../Account/ViewAll/ViewAllAccounts.html";
};

function navigateToDepositIntoAnAccount() {
    window.location.href = "../Account/Deposit/Deposit.html";
};

function navigateToWithdrawFromAnAccount() {
    window.location.href = "../Account/Withdraw/Withdraw.html";
};

function navigateToTransferBetweenAccounts() {
    window.location.href = "../Account/Transfer/Transfer.html";
};

function navigateToDeleteAnAccount() {
    window.location.href = "../Account/Delete/DeleteAccount.html";
};
