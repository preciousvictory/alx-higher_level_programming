$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    for (let lis = 0; lis < data.results.length; lis++) {
        $('UL#list_movies').append("<li>" + data.results[lis].title + "</li>");
    }
});