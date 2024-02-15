// Wait for the document to be fully loaded
$(document).ready(() => {
  // Find the <header> element
  const headerElement = $('header');

  // Adds the 'red' class to <header> element when user clicks on 'div#red_header' element
  $('DIV#red_header').click(() => {
    headerElement.addClass('red');
  });
});
