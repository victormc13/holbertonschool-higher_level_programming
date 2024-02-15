// Wait for the document to be fully loaded
$(document).ready(() => {
  // Find the 'DIV#character' element
  const textContainer = $('DIV#character');
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  // Fetch the character data from the API
  $.get(url, (data) => {
    textContainer.text(data.name);
  });
});
