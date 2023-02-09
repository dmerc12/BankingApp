function resetInputs() {
    document.getElementById("updatedFirstNameInput").value = "";
    document.getElementById("updatedLastNameInput").value = "";
    document.getElementById("updatedPasswordInput").value = "";
    document.getElementById("updatedEmailAddressInput").value = "";
    document.getElementById("updatedPhoneNumberInput").value = "";
    document.getElementById("updatedAddressInput").value = "";
};

if (!window.sessionStorage.getItem("sessionId")) {
    alert("You do not have access to this page! Please continue to log in or create your own credentials!");
    window.location.href = "../ManageLogin/Login.html";
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
        window.location.href = "../ManageLogin/Login.html";
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`${apiResponse.message}`);
        if (apiResponse.message === "Session has expired, please log in!") {
            window.sessionStorage.removeItem("sessionId");
            alert("Goodbye!");
            window.location.href = "../ManageLogin/Login.html";
        };
    } else {
        alert("Something went horribly wrong...");
        window.sessionStorage.removeItem("sessionId");
        alert("Goodbye!");
        window.location.href = "../ManageLogin/Login.html";
    };
};

async function loadCurrentInformation() {
    const loadCurrentInformationURL = "http://127.0.0.1:5000/load/customer/info";

    const sessionId = window.sessionStorage.getItem("sessionId");

    loadInfoDictionary = {
        "sessionId": sessionId
    };

    let loadCurrentInfoRequest = {
        method: "PATCH",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(loadInfoDictionary)
    };

    const response = await fetch(loadCurrentInformationURL, loadCurrentInfoRequest);

    if (response.status === 201) {
        const apiResponse = await response.json();
        populateCurrentInfo(apiResponse);
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

function populateCurrentInfo(apiResponse) {
    firstNameInput = document.getElementById("updatedFirstNameInput");
    lastNameInput = document.getElementById("updatedLastNameInput");
    emailInput = document.getElementById("updatedEmailAddressInput");
    phoneNumberInput = document.getElementById("updatedPhoneNumberInput");
    addressInput = document.getElementById("updatedAddressInput");
    
    firstNameInput.value = apiResponse.firstName;
    lastNameInput.value = apiResponse.lastName;
    emailInput.value = apiResponse.email;
    phoneNumberInput.value = apiResponse.phoneNumber;
    addressInput.value = apiResponse.address;
};

async function updateCustomer() {
    // initializing URL varible
    const updateCustomerURL = "http://127.0.0.1:5000/update/customer";

    // grabbing input from the DOM
    const sessionId = window.sessionStorage.getItem("sessionId");
    const updatedFirstName = document.getElementById("updatedFirstNameInput").value;
    const updatedLastName = document.getElementById("updatedLastNameInput").value;
    const updatedPassword = document.getElementById("updatedPasswordInput").value;
    const updatedEmailAddress = document.getElementById("updatedEmailAddressInput").value;
    const updatedPhoneNumber = document.getElementById("updatedPhoneNumberInput").value;
    const updatedAddress = document.getElementById("updatedAddressInput").value;

    // preparing JSON
    updateCustomerDictionary = {
        "sessionId": sessionId,
        "firstName": updatedFirstName,
        "lastName": updatedLastName,
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
        window.location.href = "../../Home/CustomerHome.html";
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