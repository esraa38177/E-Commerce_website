document.addEventListener('DOMContentLoaded', function() {
    console.log("Website loaded!");

    // Example of dynamically updating a cart counter (can be extended as needed)
    let cartCounter = document.getElementById('cart-counter');
    if(cartCounter) {
        cartCounter.innerHTML = localStorage.getItem('cartCount') || '0';
    }

    // Other JavaScript functionalities can go here (e.g., cart management)
});
