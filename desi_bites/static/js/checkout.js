// Function to display cart totals from local storage
function getTotal() {
    var storedTotal = localStorage.getItem('total');
    
    // Update the displayed total on the page
    if (storedTotal) {
        document.getElementById('total').innerText = `₹${storedTotal}`;
    }
}

// Call the function to display cart totals from local storage
getTotal();

    // Function to get cart items from local storage
    function getCartItems() {
        return JSON.parse(localStorage.getItem('cart')) || [];
    }


// Function to handle form submission
function submitOrderForm() {
    var cartItems = getCartItems();
    var total = localStorage.getItem('total');

    console.log(total)

    // Extract relevant data from cart items
    var itemsData = cartItems.map(item => ({
        id: item.id,
        name: item.name,
        quantity: item.quantity,
    }));

    // Extract shipping details from the form
    var fullName = document.getElementById('username').value;
    var phone = document.getElementById('phone').value;
    var streetAddress = document.getElementById('streetaddress').value;
    var postcodeZip = document.getElementById('postcodezip').value;


    // Prepare data for form submission
    var formData = new FormData();
    formData.append('items', JSON.stringify(itemsData));
    formData.append('total', total);
    formData.append('fullName', fullName);
    formData.append('phone', phone);
    formData.append('streetAddress', streetAddress);
    formData.append('postcodeZip', postcodeZip);
    

    // Make a POST request to your Django backend
    fetch('/your-django-endpoint/', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server (e.g., show a confirmation message)
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
