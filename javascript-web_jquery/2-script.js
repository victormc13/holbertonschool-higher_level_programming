// Wait for the document to be fully loaded
$(document).ready(() => {
  // Find the <header> element
  const headerElement = $('header');

  // Set the text color to red (#FF0000) when clicks on 'div#red_header' element
  $('DIV#red_header').click(() => {
    headerElement.css('color', '#FF0000');
  });
});
