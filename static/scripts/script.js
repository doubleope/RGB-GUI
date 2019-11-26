$(function() {
    $('a#process').bind('click', function() {
      $.getJSON('/getInfo', function(data) {
        console.log(data);
        $("#result").text(JSON.stringify(data, undefined, 10));
        $(document).ready(function() {
          $('#result').each(function(i, e) {hljs.highlightBlock(e)});
       });
      });
      return false;
    });
  });