// Wait for the document to be fully loaded
$(document).ready(() => {
  // Find the 'UL#list_movies' element
  const unorderedList = $('UL#list_movies');
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  // Fetch the movie data from the API
  $.get(url, (data) => {
    data.results.forEach((movie) => {
      unorderedList.append(`<li>${movie.title}</li>`);
    });
  });
});
