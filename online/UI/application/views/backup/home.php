<html>
	<head>
		<meta charset="utf-8">
	<title><?=$first?></title>
	</head>
	<body>
		<div>
			<h1>新闻列表</h1>
			<?php foreach($list as $item):?>
			<ol><?=$item?></ol>
			<?php endforeach;?>
		</div>
	</body>
</html>