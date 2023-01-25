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
