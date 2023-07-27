// document.querySelector("DIV#red_header").onclick = function () {
//     document.querySelector("header").style.color = "#FF0000";
// }
$("DIV#red_header").click(function() {
    $("header").css("color", "#FF0000");
})