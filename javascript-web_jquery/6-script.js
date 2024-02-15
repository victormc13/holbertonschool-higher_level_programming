// Wait for the document to be fully loaded
$(document).ready(() => {
  // Find the <header> element
  const headerElement = $('header');

  // Updates the text of the <header> element to 'New Header!!!'
  $('DIV#update_header').click(() => {
    headerElement.text('New Header!!!');
  });
});
