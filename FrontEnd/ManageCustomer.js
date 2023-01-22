
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
    window.location.href = "Login.html";
};

async function doLogout() {
    // initializing URL varible
    logoutURL = "http://127.0.0.1:5000/logout"

    // grabbing input from the DOM
    const sessionId = window.sessionStorage.getItem("sessionId");

    // preparing JSON
    logoutDictionary = {
        "sessionId": sessionId
    };

    // preparing request
    let logoutRequest = {
        method: "DELETE",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(logoutDictionary)
    };

    // sending request and awaiting response
    const response = await fetch(logoutURL, logoutRequest)

    // handling API response approapriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        window.sessionStorage.removeItem("sessionId");
        alert("Goodbye!");
        window.location.href = "Login.html";
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
        if (apiResponse.message === "Session has expired, please log in!") {
            window.sessionStorage.removeItem("sessionId");
            alert("Goodbye!");
            window.location.href = "Login.html";
        };
    } else {
        alert("Something went horribly wrong...");
        window.sessionStorage.removeItem("sessionId");
        alert("Goodbye!");
        window.location.href = "Login.html";
    };
};

function goHome() {
    window.location.href = "CustomerHome.html";
};

function resetInputs() {
    document.getElementById("updatedFirstNameInput").value = "";
    document.getElementById("updatedLastNameInput").value = "";
    document.getElementById("updatedUsernameInput").value = "";
    document.getElementById("updatedPasswordInput").value = "";
    document.getElementById("updatedEmailAddressInput").value = "";
    document.getElementById("updatedPhoneNumberInput").value = "";
    document.getElementById("updatedAddressInput").value = "";
};

async function updateCustomer() {
    // initializing URL varible
    const updateCustomerURL = "http://127.0.0.1:5000/update/customer";

    // grabbing input from the DOM
    const sessionId = window.sessionStorage.getItem("sessionId");
    const updatedFirstName = document.getElementById("updatedFirstNameInput").value;
    const updatedLastName = document.getElementById("updatedLastNameInput").value;
    const updatedUsername = document.getElementById("updatedUsernameInput").value;
    const updatedPassword = document.getElementById("updatedPasswordInput").value;
    const updatedEmailAddress = document.getElementById("updatedEmailAddressInput").value;
    const updatedPhoneNumber = document.getElementById("updatedPhoneNumberInput").value;
    const updatedAddress = document.getElementById("updatedAddressInput").value;

    // preparing JSON
    updateCustomerDictionary = {
        "sessionId": sessionId,
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
        body: JSON.stringify(updateCustomerDictionary)
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
        if (apiResponse.message === "Session has expired, please log in!") {
            doLogout();
        };
        resetInputs();
    } else {
        alert("Something went horribly wrong...");
        resetInputs();
    };
};

async function deleteCustomer() {
     // initializing URL varible
     const deleteCustomerURL = "http://127.0.0.1:5000/delete/customer";

     // preparing JSON
     deleteCustomerDictionary = {
         'sessionId': window.sessionStorage.getItem("sessionId")
     };
 
     // preparing request
     let deleteCustomerRequest = {
         method: "DELETE",
         headers: {'Content-Type': "application/json"},
         body: JSON.stringify(deleteCustomerDictionary)
     };
 
     // sending request and awaiting response
     const response = await fetch(deleteCustomerURL, deleteCustomerRequest);
 
     // handling API response approapriately
     if (response.status === 201) {
         const apiResponse = await response.json();
         alert("Your information has been successfully delteted!");
         window.location.href = "Login.html";
     } else if (response.status === 400) {
         const apiResponse = await response.json();
         alert(`${apiResponse.message}`);
         if (apiResponse.message === "Session has expired, please log in!") {
            doLogout();
        };
     } else {
         alert("Something went horribly wrong...");
     };
};
