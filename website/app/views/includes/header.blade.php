<?php
	$a_home = (Request::path()==="/") ? "active" : "";
	$a_articlelist = (Request::path()==="article/list") ? "active" : "";
	$a_about = (Request::path()==="about") ? "active" : "";
	$a_contact = (Request::path()==="contact") ? "active" : "";
?>

<div class="container">
	<div class="navbar-header">
		<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
			<span class="sr-only">Toggle navigation</span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
		</button>
		<a class="navbar-brand" href="#">5W1H</a>
	</div>
	<div class="navbar-collapse collapse">
		<ul class="nav navbar-nav">
			<li class="{{$a_home}}"><a href="/">Extractor</a></li>
			<!-- <li class="{{$a_articlelist}}"><a href="/article/list">Articles</a></li> -->
		</ul>
	</div><!--/.nav-collapse -->
</div>
