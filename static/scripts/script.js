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

  $(function() {
    $('a#save').bind('click', function() {
    $.getJSON('/postClusterInfo', {
      cluster_name: $('input[name="cluster_name"]').val(),
      cluster_type: $('input[name="cluster_type"]').val(),
      ip: $('input[name="ip"]').val(),
      port: $('input[name="port"]').val(),
      mac_address: $('input[name="mac_address"]').val()
    }, function() {
      return false
    });
    return false;
    });
  });