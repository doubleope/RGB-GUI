$(function() {
    $('a#process').bind('click', function() {
      $.getJSON('/getInfo', function(data) {
        $("#result").text(data.result);
      });
      return false;
    });
  });