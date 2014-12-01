
function getRandomNews() {
	$.ajax({
		url: "/api/randomnews",
		data: {
			zipcode: 97201
		},
		success: function( data ) {
			$( "#inputNews" ).html(data["news"]);
		}
	});
}