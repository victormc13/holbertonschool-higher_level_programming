// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // Select the tag with id red_header and header element
  const liElement = '<li>Item</li>'
  const myList = document.querySelector(".my_list")
  const addItem = document.querySelector("#add_item")
  // Add a click event listener to the red_header tag
  addItem.addEventListener("click", () => {
    // Adds the class 'red' to the header element when the user clicks
    myList.insertAdjacentHTML("beforeend", liElement)
  });
});

