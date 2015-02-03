@extends('layouts.default')
@section('content')
    {{ HTML::style('css/extractor.css') }}
    {{ HTML::script('js/extractor.js') }}
    <div class="col-sm-1"></div>
    <div class="col-sm-10">
        <div class="row">
            <div class="paddingBox col-sm-2"></div>
            <div id="inputNewsBox" class="col-sm-8">
    			<h2>Berita</h2>
                <hr>
                <div class="form-group">
            		<textarea id="inputNews" class="form-control" rows="22" placeholder="input berita disini" name="what"></textarea>
            	</div>
                <div class="form-group">
            		<button class="btn btn-info pull-right" onclick="submitNews()">SUBMIT</button>
            	</div>
            </div>
            <div id="info5w1hBox" class="col-sm-6">
                <h2>Info 5W1H</h2>
                <hr>
                <form id="info_form" class="form-horizontal" role="form" method="post" action="/info">
                    <input type="hidden" class="form-control" id="inputArticleId" placeholder="What" name="article_id" value="">
                    <div class="form-group">
                        <label class="col-sm-2 control-label">What</label>
                        <div class="col-sm-10">
                            <textarea id="outputWhat" class="form-control" rows="4" placeholder="none" name="what" readonly=""></textarea>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-2 control-label">Who</label>
                        <div class="col-sm-10">
                            <textarea id="outputWho" class="form-control" rows="2" placeholder="none" name="who" readonly=""></textarea>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-2 control-label">When</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="outputWhen" placeholder="none" name="when" readonly="">
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-2 control-label">Where</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="outputWhere" placeholder="none" name="where" readonly="">
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-2 control-label">Why</label>
                        <div class="col-sm-10">
                            <textarea id="outputWhy" class="form-control" rows="4" placeholder="none" name="why" readonly=""></textarea>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-2 control-label">How</label>
                        <div class="col-sm-10">
                            <textarea id="outputHow" class="form-control" rows="4" placeholder="none" name="how" readonly=""></textarea>
                        </div>
                    </div>
                </form>
            </div>
    	</div>
    </div>
    <div class="col-sm-1"></div>
    {{ HTML::script('packages/jquery/jquery.min.js') }}
    {{ HTML::script('packages/jquery-ui/jquery-ui.js') }}
@stop