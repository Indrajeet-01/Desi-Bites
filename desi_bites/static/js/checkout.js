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