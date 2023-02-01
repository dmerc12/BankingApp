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

function toggleVisibleLoginOrLogoutNav() {
    
}

function toggleVisibleLoginOrLogoutNav() {
    toggleVisibleNav = document.getElementById("navLoginRegisterLogout");
    sessionId = window.sessionStorage.getItem("sessionId")

    toggleVisibleNav.innerHTML = "";
    if (sessionId == null) {
        const loginButton = document.createElement("a");
        loginButton.class = "nav-item nav-link";
        loginButton.href = "Login.html";
        loginButton.innerHTML = "Login";
        toggleVisibleNav.appendChild(loginButton);

        const registerButton = document.createElement("a");
        registerButton.class = "nav-item nav-link";
        registerButton.href = "NewCustomer.html";
        registerButton.innerHTML = "Register";
        toggleVisibleNav.appendChild(registerButton);
    } else {
        const logoutButton = document.createElement("a");
        logoutButton.class = "nav-item nav-link";
        logoutButton.href = "Login.html";
        logoutButton.innerHTML = "Logout";
        logoutButton.onclick = doLogout();
        toggleVisibleNav.appendChild(logoutButton);
    };
};

if (!window.sessionStorage.getItem("sessionId")) {
    alert("You do not have access to this page! Please continue to log in or create your own credentials!");
    window.location.href = "Login.html";
};

function goHome() {
    window.location.href = "CustomerHome.html";
};

function navigateToManageAccounts() {
    window.location.href = "ManageAccounts.html";
};

function navigateToManageCustomer() {
    window.location.href = "ManageCustomer.html";
};

function navigateToTransactions() {
    window.location.href = "Transactions.html"
};
