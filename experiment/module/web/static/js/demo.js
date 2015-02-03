
function getRandomNews() {
	$.ajax({
		url: "/api/randomnews",
		success: function( data ) {
			$("#inputNews").val(data["news"]);
		}
	});
}


function getWhen() {
	$.ajax({
		type: "POST",
		url: "/api/when",
		data: {
			text: addslashes($("#inputNews").val())
		},
		success: function( data ) {
			temp = ""
			data["when"].forEach(function(e,i,a){
				temp = temp + "<li class=\"list-group-item\">"+e+"</li>";
			});
			$("#outputNews").html(temp);
		}
	});
}

function addslashes( str ) {
    return (str + '').replace(/[\\"']/g, '\\$&').replace(/\u0000/g, '\\0');
}