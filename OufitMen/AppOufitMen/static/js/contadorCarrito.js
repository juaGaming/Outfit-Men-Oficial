const cart = [];
function addToCart(productName) {
    cart.push(productName);
    updateCartCount();
}
function updateCartCount() {
    const cartCount = document.getElementById("cart-count");
    cartCount.textContent = cart.length;
}
const addToCartButtons = document.querySelectorAll(".btn-add-to-cart");
addToCartButtons.forEach((button) => {
    button.addEventListener("click", function () {
        const productName = this.dataset.productName;
        addToCart(productName);
    });
});