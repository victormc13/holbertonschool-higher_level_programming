// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // Select the tag with id red_header and header element
  const header = document.querySelector("header");
  const redHeader = document.getElementById("red_header");
  // Add a click event listener to the red_header tag
  redHeader.addEventListener("click", () => {
    // Update the text color of the header element to red
    header.style.color = "#FF0000"
  });
});
