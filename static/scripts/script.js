var j = jQuery_1_4_2

function displayClusterInfo(data){
  j("#result").text(JSON.stringify(data, undefined, 10));
        j(document).ready(function() {
          j('#result').each(function(i, e) {hljs.highlightBlock(e)});
       });
}


j(function() {
  j('a#get-cluster-data').bind('click', function() {
    j.getJSON('/show_data_center_info', function(data) {
        displayClusterInfo(data)
      });
      return false;
    });
  });


function ValidateIPaddress(inputText) {
  var ipformat = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;
  if(inputText.value.match(ipformat)) {
    document.form1.text1.focus();
    return true;
  }
  else {
    alert("You have entered an invalid IP address!");
    document.form1.text1.focus();
    return false;
  }
}
alert("yes")

j(function() {
  j('a#save').bind('click', function() {
    j.getJSON('/post_cluster_info', {
    cluster_name: j('input[name="cluster_name"]').val(),
    cluster_type: j('#type').find('option:selected').text(),
    ip: j('input[name="ip"]').val(),
    port: j('input[name="port"]').val(),
    mac_address: j('input[name="mac_address"]').val()
  }, function(data) {
    if(data == "mac error"){
      alert("Enter a valid mac address")
    }else {
      displayClusterInfo(data)
    }
  });
  return false;
  });
});