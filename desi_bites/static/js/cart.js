
// Function to handle quantity changes
function updateQuantity(itemId, operation, step) {
    var quantityField = document.getElementById('quantity' + itemId);
    var currentQuantity = parseInt(quantityField.value);

    if (operation === 'plus') {
        quantityField.value = (currentQuantity + step).toString();
    } else if (operation === 'minus' && currentQuantity > step) {
        quantityField.value = (currentQuantity - step).toString();
    }

    // If you need to do something else with the quantity, add your logic here
}

// Add event listeners for quantity buttons
document.querySelectorAll('.quantity-left-minus').forEach(function (button) {
    button.onclick = function () {
        var itemId = button.getAttribute('data-field').replace('quantity', '');
        updateQuantity(itemId, 'minus', 1);
    };
});

document.querySelectorAll('.quantity-right-plus').forEach(function (button) {
    button.onclick = function () {
        var itemId = button.getAttribute('data-field').replace('quantity', '');
        updateQuantity(itemId, 'plus', 1);
    };
});


    // Function to get cart items from local storage
    function getCartItems() {
        return JSON.parse(localStorage.getItem('cart')) || [];
    }

     // Function to update the cart length
    function updateCartLength() {
        var cartItems = getCartItems();
        var cartLengthElement = document.getElementById('cart-length');
        if (cartLengthElement) {
            cartLengthElement.innerText = cartItems.length;
        }
    }

    // Function to calculate the total price for a cart item
    function calculateTotalPrice(item) {
        return (parseFloat(item.price) * parseInt(item.quantity)).toFixed(2);
    }

    // Function to remove an item from the cart
    function removeCartItem(itemId) {
        var cartItems = getCartItems();
        var updatedCart = cartItems.filter(item => item.id !== itemId);
        localStorage.setItem('cart', JSON.stringify(updatedCart));
        displayCart();
    }

    // Function to display cart items
    function displayCart() {
        var cartItems = getCartItems();
        var cartTableBody = document.getElementById('cart-table-body');

        // Clear existing table rows
        cartTableBody.innerHTML = '';

        // Loop through each cart item and add a row to the table
        cartItems.forEach(item => {
            var row = document.createElement('tr');
            row.innerHTML = `
                
                <td class="image-prod"><div class="img" style="background-image:url(${item.image});"></div></td>
                <td class="product-name">
                    <h3>${item.name}</h3>
                    
                </td>
                <td class="price">₹${item.price}</td>
                <td class="quantity">
                    <div class="input-group mb-3">
                        <input type="text" name="quantity" class="quantity form-control input-number" value="${item.quantity}" min="1" max="100">
                    </div>
                </td>
                <td class="total">₹${calculateTotalPrice(item)}</td>
                <td class="product-remove"><a href="#" onclick="removeCartItem('${item.id}')"><span class="icon-close"></span></a></td>
            `;
            cartTableBody.appendChild(row);
        });

        // Calculate and display cart totals
        var subtotal = cartItems.reduce((sum, item) => sum + parseFloat(item.price) * parseInt(item.quantity), 0).toFixed(2);
        var total = (parseFloat(subtotal) + parseFloat(40) );

        localStorage.setItem('total', total)

        document.getElementById('subtotal').innerText = `₹${subtotal}`;
        document.getElementById('total').innerText = `₹${total}`;
    }

    // Function to add an item to the cart
    function addToCart(itemId, itemName, itemPrice, itemImage) {
        var quantity = document.getElementById('quantity' + itemId).value;
        var cartItem = {
            id: itemId,
            name: itemName,
            price: itemPrice,
            quantity: quantity,
            image: itemImage
            // Add other properties as needed
        };

        // Get existing cart items from local storage
        var cartItems = JSON.parse(localStorage.getItem('cart')) || [];

        // Check if the item is already in the cart
        var existingItemIndex = cartItems.findIndex(item => item.id === itemId);

        if (existingItemIndex !== -1) {
            // Update quantity if item is already in the cart
            cartItems[existingItemIndex].quantity = parseInt(cartItems[existingItemIndex].quantity) + parseInt(quantity);
        } else {
            // Add new item to the cart
            cartItems.push(cartItem);
        }

        // Save updated cart to local storage
        localStorage.setItem('cart', JSON.stringify(cartItems));

        // Update the cart display
        updateCartLength();
        displayCart();
    }

    // Initial display when the page loads
    updateCartLength();
    displayCart();

