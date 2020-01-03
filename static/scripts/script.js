var j = jQuery_1_4_2

j(function() {
  j('a#process').bind('click', function() {
    j.getJSON('/getInfo', function(data) {
        console.log(data);
        j("#result").text(JSON.stringify(data, undefined, 10));
        j(document).ready(function() {
          j('#result').each(function(i, e) {hljs.highlightBlock(e)});
       });
      });
      return false;
    });
  });

  j(function() {
    j('a#save').bind('click', function() {
      j.getJSON('/postClusterInfo', {
      cluster_name: j('input[name="cluster_name"]').val(),
      cluster_type: j('input[name="cluster_type"]').val(),
      ip: j('input[name="ip"]').val(),
      port: j('input[name="port"]').val(),
      mac_address: j('input[name="mac_address"]').val()
    }, function() {
      return false
    });
    return false;
    });
  });