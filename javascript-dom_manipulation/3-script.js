// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // Select the tag with id red_header and header element
  const header = document.querySelector("header");
  const toggleHeader = document.getElementById("toggle_header");
  // Add a click event listener to the red_header tag
  toggleHeader.addEventListener("click", () => {
    // Adds the class 'red' to the header element when the user clicks
    greenClass = header.classList.contains("green")
    if (greenClass) {
      header.classList.replace("green", "red")
    }
    else {
      header.classList.replace("red", "green")
    }
  });
});