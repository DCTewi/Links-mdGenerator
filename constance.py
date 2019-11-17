#coding=utf8

prevcss = """<style>
	.link-content li
	{
		display: inline-block;
		vertical-align: top;
		text-align: center;
		width: 100px;
		height: 110px;
		font-size:14px;
		margin-bottom:10px;
		list-style-type: none;
	}
	.link-content li img
	{
		border-radius:100%;
		margin-bottom:5px;
		width:64px;
		height=64px;
		transition:0.5s;
		-webkit-transtion:1.5s;
	}
	.link-content li span
	{
		display:block;
        text-align: center;
	}
	.link-content li:hover img
	{
		transform:rotate(360deg);
		-webkit-transform:rotate(360deg);
	}
    .clearfix:after 
    {
		visibility: hidden;
		display: block;
		font-size: 0;
		content: "";
		clear: both;
		height: 0;
    }
</style>
<script src="https://cdn.staticfile.org/jquery/1.10.2/jquery.min.js"></script>
"""

ulprev = """
<div class=\"links\">
<ul class=\"link-content clearfix\">
"""

ultail = """
</ul>
</div>
<script>
    $(".link-content li").each(function(){
        while (parseInt(Math.random() * 2) == 0){
            $(this).prependTo($(this).parent());
        }
    });
</script>
"""
