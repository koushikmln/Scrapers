<!DOCTYPE html>
<html lang="en" class="no-js">
	<head>
		<meta charset="UTF-8" />
		<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"> 
		<meta name="viewport" content="width=device-width, initial-scale=1.0"> 
		<title>Kampayer</title>
		<link rel="stylesheet" type="text/css" href="css/default.css" />
		<link rel="stylesheet" type="text/css" href="css/component.css" />
		<script src="js/modernizr.custom.js"></script>
	</head>
	<body>
		<div class="kampayer">
			<div class="shopsmart">Shop Smart!</div>
			<?php 
				 $store="Flipkart";
				 $cost="10000";
				 $saving="1813";
				 echo "<div class='productstore'>Buy this product on ".$store." for `".$cost." and save `".$saving."   </div>";
			?>
		<ul id="cbp-tm-menu" class="cbp-tm-menu">

				<li><a href="http://www.kampayer.in"><img src="images/buynow.png"></li>
				<li>
					<a href="#"><img src="images/kplogo.png"></a>
					<ul class="cbp-tm-submenu">
						<li><a href="#" class="cbp-tm">Flipkart</a></li>
						<li><a href="#" class="cbp-tm">Amazon</a></li>
						<li><a href="#" class="cbp-tm">eBay</a></li>
						<li><a href="#" class="cbp-tm">Snapdeal</a></li>
						<li><a href="#" class="cbp-tm">Homeshop18</a></li>
						<li><a href="#" class="cbp-tm">Infibeam</a></li>
					</ul>
				</li>
			</ul>
		</div>
		<script src="js/cbpTooltipMenu.min.js"></script>
		<script>
			var menu = new cbpTooltipMenu( document.getElementById( 'cbp-tm-menu' ) );
		</script>
	</body>
</html>
