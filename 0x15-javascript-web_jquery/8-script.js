const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
  const reslt = data.results;
  for (let i = 0; i < reslt.length; i++) {
    $('UL#list_movies').append('<li>' + reslt[i].title + '</li>');
  }
});
