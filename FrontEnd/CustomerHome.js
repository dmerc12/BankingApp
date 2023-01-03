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

function doLogout() {
    window.sessionStorage.removeItem("customerId");
    window.sessionStorage.removeItem("firstName");
    window.sessionStorage.removeItem("lastName");
    window.sessionStorage.removeItem("username");
    window.sessionStorage.removeItem("password");
    window.sessionStorage.removeItem("email");
    window.sessionStorage.removeItem("phoneNumber");
    window.sessionStorage.removeItem("address");
    alert("Goodbye!");
    window.location.href = "Login.html";
;}

function navigateToManageAccounts() {

}

function navigateToManageCustomer() {
    
}
