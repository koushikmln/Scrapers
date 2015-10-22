var addr="Address for server";
var scrpt= "Kampayer.in is under maintenance!!";
var client;
var curr_url;
var prodName;
var sourceKey;
var response_data_color = "NA";
var response_data_price = "NA";

function server_call()
{
		$.ajax({
		type:"POST",
		url:addr,
		data: {curr_url: curr_url, client : client, sourceKey: sourceKey},
		async:false,
		success: function(data)
		{
			scrpt=data;
		}
		});
}


chrome.runtime.onMessage.addListener(function(request,sender,sendResponse)
{
	if(request.sent_from == 'con')
	{
		curr_url = request.curr_url;
		sourceKey = curr_url.split('?')[1].split('&')[0].split('=')[1];
		if (curr_url.search("flipkart.com")!==-1){
			client = "FK";
			}
		else if (curr_url.search("amazon.in")!==-1){
			client = "AMZ";
			}
		
	
		prodName = request.prod_name;
		
		server_call();
		
		sendResponse(scrpt);
		return true;

	}	
});
