curr_url=document.URL;
var newdiv = document.createElement('div');
newdiv.setAttribute('id','Kampayer');
var bar=document.getElementById("fk-header"); // fk-mainhead-id
//var kampayer_pName;
var prod_name;
//var prod_price;
var storeSpecs = ["NA", "NA", "NA", "NA"];

if(curr_url.search("flipkart.com")!==-1)
{
	prod_name=document.getElementsByClassName("mprod-summary-title fksk-mprod-summary-title")[0].getElementsByTagName("h1")[0].innerHTML;
	//prod_price = parseInt(document.getElementsByClassName("fk-font-verybig pprice fk-bold")[0].innerHTML);
}


function getStoresDesc(storeData)
{
	split_client_data = storeData.replace(/^\s+|\s+|\r+|\n+|"/g, '').split('|');
		pr_client = split_client_data[0];
		pr_url = split_client_data[1].replace(/^\s+|\s+|\r+|\n+|"|^\(|\)$|\\/g, '');
		if (split_client_data.length > 3) {pr_color = split_client_data[3].replace(/^\s+|\r+|\n+|"|^\(|\)$|\\/g, '');} else { pr_color = "NA";}
		if (split_client_data.length > 4) {pr_price = parseInt(split_client_data[4].replace(/^\s+|\s+|\r+|\n+|"|Rs.|Rs|,|\\/g, ''));} else { pr_price = 10000000;}
		
		return [pr_client, pr_url, pr_color, pr_price];
}


chrome.runtime.sendMessage({sent_from:'con', prod_name:prod_name, curr_url:curr_url},function (response)
{
	
	newdiv.style.background = "-webkit-linear-gradient(top, #88d600, #30a700)";
	newdiv.style.width = "100%";
	newdiv.style.position="fixed";
	newdiv.style.zIndex = "1000";
	newdiv.style.left = "0";
	newdiv.style.height="47px";
	
	///////////////////////////
	
	var dropdown_menu = '';
	var bestPrice = 100000000;
	var bestClient = "FK";
	var bestColor = "Black";
	var bestURL = "NA"
	var count = 0;
	stores = response.split('||');
	for (i=0, len = stores.length; i<len; i++)
	{
		storeSpecs  = getStoresDesc(stores[i]);
		
		if (storeSpecs[3] < bestPrice)
		{
			bestURL = storeSpecs[1];
			bestPrice = storeSpecs[3];
			bestClient = storeSpecs[0];
			bestColor = storeSpecs[2];
		}
		
		if (storeSpecs[0]=="HS18" || storeSpecs[0]=="IN")
		{
			if (count == 0){	 count = count +1; dropdown_menu = dropdown_menu + '<ul class="dropdown-menu" style="height:400px; overflow-y:scroll;"><li><a href="'+storeSpecs[1]+'">' + storeSpecs[0] + ',' + storeSpecs[2] + ',' + storeSpecs[3] + '</a></li>';}
			else { 	count = count+1;dropdown_menu = dropdown_menu + '<li class="divider"></li><li><a href="'+ storeSpecs[1].replace('m','M') +'">'+ storeSpecs[0] + ',' + storeSpecs[2] + ',' + storeSpecs[3] + '</a></li>';}
		}
		else
		{
			if (count == 0){
				count = count +1; dropdown_menu = dropdown_menu + '<ul class="dropdown-menu" style="height:400px; overflow-y:scroll;"><li><a href="'+storeSpecs[1]+'">' + storeSpecs[0] + ',' + storeSpecs[2] + ',' + storeSpecs[3] + '</a></li>';
			}
			else{
				count = count+1;dropdown_menu = dropdown_menu + '<li class="divider"></li><li><a href="'+storeSpecs[1]+'">'+  storeSpecs[0] + ',' + storeSpecs[2] + ',' + storeSpecs[3] + '</a></li>';
			}
		
		}
		
	}
	
	////////////////////////////
	
	newdiv.innerHTML = '<link rel="stylesheet" href="http://ec2-54-187-94-39.us-west-2.compute.amazonaws.com/kamPayer_1/bootstrap-3.1.1/dist/css/bootstrap.min.css"><link rel="stylesheet" href="http://ec2-54-187-94-39.us-west-2.compute.amazonaws.com/kamPayer_1/bootstrap-3.1.1/dist/css/bootstrap-theme.min.css"><script src="http://ec2-54-187-94-39.us-west-2.compute.amazonaws.com/kamPayer_1/jquery.js"></script><script src="http://ec2-54-187-94-39.us-west-2.compute.amazonaws.com/kamPayer_1/bootstrap.min.js"></script><div class="extension"><link rel="stylesheet" type="text/css" href="http://ec2-54-187-94-39.us-west-2.compute.amazonaws.com/kamPayer_1/css/default.css"><div class="shopsmart">Shop Smart!</div> <div class="productstore"> Buy this product at '+ bestClient+ ' of color '+ bestColor +' for '+ bestPrice +'</div> <a href="'+ bestURL+'" style="float:left;"><img src="http://ec2-54-187-94-39.us-west-2.compute.amazonaws.com/kamPayer_1/images/buynow.png" alt="Buy Now"></a><div class="btn-group" style="float:left;"><button data-toggle="dropdown" class="btn btn-default dropdown-toggle" id="kplogo"><img src="http://ec2-54-187-94-39.us-west-2.compute.amazonaws.com/kamPayer_1/images/kplogo.png" alt="other options"></button>' + dropdown_menu + '</ul></div></div>'
	
	//newdiv.innerHTML = '<script src="jquery.js"></script><script src="cbpTooltipMenu.min.js"><script type="text/javascript" src="script.js"></script></script><link rel="stylesheet" type="text/css" href="http://127.0.0.1/extension/css/default.css" /><link rel="stylesheet" type="text/css" href="http://127.0.0.1/extension/css/component.css" /><script src="modernizr.custom.js"></script><div class="kampayer"><div class="shopsmart">Shop Smart!</div><div class="productstore">Buy this product on Flipkart for `10000 and save `1813</div><ul id="cbp-tm-menu" class="cbp-tm-menu"><li><a href="http://www.kampayer.in"><img src="http://127.0.0.1/extension/images/buynow.png"></li><li><a href="#"><img src="http://127.0.0.1/extension/images/kplogo.png"></a><ul class="cbp-tm-submenu" id="menu"><li><a href="#" class="cbp-tm">Flipkart</a></li><li><a href="#" class="cbp-tm">Amazon</a></li><li><a href="#" class="cbp-tm">eBay</a></li><li><a href="#" class="cbp-tm">Snapdeal</a></li><li><a href="#" class="cbp-tm">Homeshop18</a></li><li><a href="#" class="cbp-tm">Infibeam</a></li></ul></li></ul></div>'

	var list=document.getElementsByTagName("html")[0];
	(document.html||document.documentElement).insertBefore(newdiv,list.childNodes[1]);
	var script = document.createElement('script');
	
	if(bar){
	script.textContent = '$(document).ready(function(){$("#Kampayer").fadeIn(700); $("#'+(bar.id)+'").animate({marginTop:"47px"},0);});';	
	}
	script.type="text/javascript";
	(document.head||document.documentElement).appendChild(script);
});

