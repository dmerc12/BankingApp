
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

function resetInputs() {
    document.getElementById("updatedFirstNameInput").value = "";
    document.getElementById("updatedLastNameInput").value = "";
    document.getElementById("updatedUsernameInput").value = "";
    document.getElementById("updatedPasswordInput").value = "";
    document.getElementById("updatedEmailAddressInput").value = "";
    document.getElementById("updatedPhoneNumberInput").value = "";
    document.getElementById("updatedAddressInput").value = "";
    document.getElementById("viewTransactionsAccountIdInput").value = "";
};

async function updateCustomer() {
    // initializing URL varible
    const updateCustomerURL = "http://127.0.0.1:5000/update/customer";

    // grabbing input from the DOM
    const updatedFirstName = document.getElementById("updatedFirstNameInput").value;
    const updatedLastName = document.getElementById("updatedLastNameInput").value;
    const updatedUsername = document.getElementById("updatedUsernameInput").value;
    const updatedPassword = document.getElementById("updatedPasswordInput").value;
    const updatedEmailAddress = document.getElementById("updatedEmailAddressInput").value;
    const updatedPhoneNumber = document.getElementById("updatedPhoneNumberInput").value;
    const updatedAddress = document.getElementById("updatedAddressInput").value;

    // checking for empty inputs to fill in with existing values
    if (updatedFirstName === "") {
        updatedFirstName = window.sessionStorage.getItem("firstName");
    };
    if (updatedLastName === "") {
        updatedLastName = window.sessionStorage.getItem("lastName");
    };
    if (updatedUsername === "") {
        updatedUsername = window.sessionStorage.getItem("username");
    };
    if (updatedPassword === "") {
        updatedPassword = window.sessionStorage.getItem("password");
    };
    if (updatedEmailAddress === "") {
        updatedEmailAddress = window.sessionStorage.getItem("email");
    };
    if (updatedPhoneNumber === "") {
        updatedPhoneNumber = window.sessionStorage.getItem("phoneNumber");
    };
    if (updatedAddress === "") {
        updatedAddress = window.sessionStorage.getItem("address");
    };

    // preparing JSON
    updateCustomerJSON = {
        "customerId": window.sessionStorage.getItem(customerId),
        "firstName": updatedFirstName,
        "lastName": updatedLastName,
        "username": updatedUsername, 
        "password": updatedPassword,
        "email": updatedEmailAddress,
        "phoneNumber": updatedPhoneNumber,
        "address": updatedAddress
    };

    // preparing request
    let updateCustomerRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(updateCustomerJSON)
    };

    // sending request and awaiting response
    const response = await fetch(updateCustomerURL, updateCustomerRequest);

    // handling API response approapriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        alert("Customer information successfully updated!");
        resetInputs();
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
        resetInputs();
    } else {
        alert("Something went horribly wrong...")
        resetInputs();
    };
};

async function deleteCustomer() {
     // initializing URL varible
     const deleteCustomerURL = "http://127.0.0.1:5000/delete/customer";

     // preparing JSON
     deleteCustomerJSON = {
         'customerId': window.sessionStorage.getItem("customerId")
     };
 
     // preparing request
     let deleteCustomerRequest = {
         method: "DELETE",
         headers: {'Content-Type': "application/json"},
         body: JSON.stringify(deleteCustomerJSON)
     };
 
     // sending request and awaiting response
     const response = await fetch(deleteCustomerURL, deleteCustomerRequest);
 
     // handling API response approapriately
     if (response.status === 201) {
         const apiResponse = await response.json();
         alert("Your information has been successfully delteted!");
         doLogout();
     } else if (response.status === 400) {
         const apiResponse = await response.json();
         alert(`${apiResponse.message}`);
     } else {
         alert("Something went horribly wrong...")
     };
};