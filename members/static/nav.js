// Get a reference to the checkbox and the drawer element
const checkbox = document.getElementById('cbx-login');
const drawer = document.querySelector('#drawer');

let id; 


// Add an event listener to the checkbox for the 'change' event
checkbox.addEventListener('change', function () {
    if (!this.checked) {
        drawer.style.display = 'block'
        drawer.id = id
    } else {
        id = drawer.id
        drawer.id = 'cbx-clk'

    }
});
checkbox.click()