@extends('layouts.default')
@section('content')
    <div class="col-sm-3"></div>
    <div class="col-sm-6">
        <form class="form-horizontal" role="form" method="post" action="/login">
            <div class="form-group">
                <div class="col-sm-2"></div>
                <div class="col-sm-10">
					<h1>Login</h1>
                </div>
            </div>
			<!-- if there are login errors, show them here -->
			<p>
				{{ $errors->first('username') }}
				{{ $errors->first('password') }}
			</p>
            <div class="form-group">
                <label for="inputUsername" class="col-sm-2 control-label">Username</label>
                <div class="col-sm-10">
                    <input name="username" type="text" class="form-control" id="inputUsername" placeholder="" value="">
                </div>
            </div>
            <div class="form-group">
                <label for="inputPassword" class="col-sm-2 control-label">Password</label>
                <div class="col-sm-10">
                    <input name="password" type="password" class="form-control" id="inputPassword" placeholder="" value="">
                </div>
            </div>
            <div class="form-group">
                <div class="col-sm-2"></div>
                <div class="col-sm-10">
                    <input class="btn btn-info" name="submit" type="submit" placeholder="" value="login">
                </div>
            </div>
		</form>
    </div>
    <div class="col-sm-3"></div>
@stop