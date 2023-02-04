
async function createCustomer() {
    // initializing URL variable
    const createCustomerURL = "http://127.0.0.1:5000/create/customer"

    // grabbing inputs from DOM
    const firstName = document.getElementById("firstNameInput").value;
    const lastName = document.getElementById("lastNameInput").value;
    const username = document.getElementById("usernameInput").value;
    const password = document.getElementById("passwordInput").value;
    const email = document.getElementById("emailInput").value;
    const phoneNumber = document.getElementById("phoneNumberInput").value;
    const address = document.getElementById("addressInput").value;

    // preparing JSON
    customerJSON = {
        'firstName': firstName,
        'lastName': lastName,
        'username': username,
        'password': password,
        'email': email,
        'phoneNumber': phoneNumber,
        'address': address
    };

    // preparing request to create a new customer
    let newCustomer = {
        method: "POST",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(customerJSON)
    };

    // send request and await response
    const response = await fetch(createCustomerURL, newCustomer);

    //handling API response appropriately
    if (response.status === 201) {
        const apiResponse = await response.json();
        alert(`Customer successfully created!`);
        window.location.href = "Login.html";
    } else if (response.status === 400) {
        const apiResponse = await response.json();
        alert(`Could not create new customer, ${apiResponse.message}`);
        resetInputs();
    } else {
        alert("Something went horribly wrong...")
    }
};

function resetInputs() {
    // reset all inputs to empty
    document.getElementById("firstNameInput").value = "";
    document.getElementById("lastNameInput").value = "";
    document.getElementById("usernameInput").value = "";
    document.getElementById("password").value = "";
    document.getElementById("emailInput").value = "";
    document.getElementById("phoneNumberInput").value = "";
    document.getElementById("addressInput").value = "";
};
