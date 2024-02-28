$(document).ready(function () {
  $.getJSON(
    'https://hellosalut.stefanbohacek.dev/?lang=fr',
    function (data) {
      $.each(data.query.results, function (i, value) {
        $('DIV#hello').text(value.hello);
      });
    }
  );
});