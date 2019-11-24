$(document).ready(function(){

document.getElementById("result").innerHTML;


function update_values() {
    
    $.getJSON($SCRIPT_ROOT + '/getInfo', 
        function(data) {
            $('#result').text(data.result);
            console.log(data)
        }
    );
  
};

});
