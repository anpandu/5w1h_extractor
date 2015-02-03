<!doctype html>
<html>
<head>
	@include('includes.head')
</head>
<body>
	<div class="container col-sm-12">

        <div class="navbar navbar-default navbar-fixed-top" role="navigation">
			@include('includes.header')
		</div>

        <!-- <div class="container col-sm-12"> -->

			@yield('content')

		<!-- </div> -->

        <!-- <div class="navbar navbar-default navbar-fixed-bottom">
		</div> -->
				@include('includes.footer')

	</div>
</body>
</html>