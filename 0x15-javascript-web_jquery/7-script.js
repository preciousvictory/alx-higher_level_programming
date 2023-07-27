// $.ajax({
//     type: 'GET',
//     url: 'https://swapi.co/api/people/5/?format=json',
//     data: data,
//     success: function (data) {
//       $("DIV#character").html(data.name);
//     }
// });

$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('DIV#character').html(data['name']);
});