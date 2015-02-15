
function jsonCallback(data) {
	info = data["info"];
	dwhat = info["what"];
	dwho = info["who"];
	dwhen = info["when"];
	dwhere = info["where"];
	dwhy = info["why"];
	dhow = info["how"];
	fill5w1h($("#inputNews").val(), dwhat, dwho, dwhen, dwhere, dwhy, dhow);
}

function submitNews() {
	$("#info5w1hBox").css("display", "block");
	$(".paddingBox").css("display", "none");
	$("#inputNewsBox").removeClass("col-sm-10").addClass("col-sm-6");
	getContent($("#inputNews").val());
}

function getContent(_news) {
    $.ajax({
	    url: "http://0.0.0.0:8887/extract?text="+_news,
	    type: "GET",
	    dataType: 'jsonp',
	    processData: false,
	    CrossDomain:true,
	    async: false,
	    success: function (d) {

	    },
	    error: function (xhr, ajaxOptions, thrownError) { //Add these parameters to display the required response
	    	if (xhr.status!=200) {
	    		fill5w1h($("#inputNews").val(), "", "", "", "", "", "");
	    	}
	    	// console.log(xhr.status)
	    	// console.log(xhr)
	    	// console.log(ajaxOptions)
	    	// console.log(thrownError)
		}
	});
}

function fill5w1h(a, b, c, d, e, f, g) {
	$("#inputNews").val(a)
	$("#outputWhat").val(b)
	$("#outputWho").val(c)
	$("#outputWhen").val(d)
	$("#outputWhere").val(e)
	$("#outputWhy").val(f)
	$("#outputHow").val(g)
}

